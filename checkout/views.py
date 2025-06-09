from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse
from bag.contexts import bag_contents
from .forms import OrderForm
from .models import Order, OrderItem
from products.models import ShopPlant
import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        request.session['save_info'] = request.POST.get('save_info')
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'username': request.user.username,
        })
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(content=e, status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.order_total = 0  
            order.delivery_cost = 0  
            order.grand_total = 0
            order.save()

            bag = request.session.get('bag', {})

            for item_id, quantity in bag.items():
                plant = get_object_or_404(ShopPlant, pk=item_id)
                order_item = OrderItem(
                    order=order,
                    plant=plant,
                    quantity=quantity
                )
                order_item.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))


    else:
        bag = request.session.get('bag', {})
        if not bag:
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)  
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='gbp',
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
