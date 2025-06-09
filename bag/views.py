from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import JsonResponse
from django.contrib import messages
from products.models import ShopPlant

def view_bag(request):
    """ A view that renders the shopping bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """
    Add a quantity of the specified plant to the shopping bag
    """
    plant = get_object_or_404(ShopPlant, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified plant to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    """
    try:
        plant = get_object_or_404(ShopPlant, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        request.session['bag'] = bag

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)