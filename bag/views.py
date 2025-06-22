from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from products.models import ShopPlant


def view_bag(request):
    """ Renders the shopping bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified plant to the shopping bag
    """
    plant = get_object_or_404(ShopPlant, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Check if the item already exists in the bag
    if item_id in bag:
        # If it exists, update the quantity
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {plant.name} quantity to {bag[item_id]} in your bag.'
        )
    else:
        # If it does not exist, add it to the bag
        bag[item_id] = quantity
        messages.success(request, f'Added {plant.name} to your bag.')

    # Save the updated bag back to the session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified plant to the specified amount
    """
    plant = get_object_or_404(ShopPlant, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    # If updated qauntity is greater than 0, update the quantity in the bag
    if quantity > 0:
        bag[item_id] = quantity
        messages.info(request, f'Updated {plant.name} quantity to {quantity}.')
    # If updated quantity is 0, remove the item from the bag
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {plant.name} from your bag.')

    # Save the updated bag back to the session
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    """
    try:
        plant = get_object_or_404(ShopPlant, pk=item_id)
        bag = request.session.get('bag', {})

        # If the item is in the bag, remove it
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(request, f'Removed {plant.name} from your bag.')
        return HttpResponse(status=200)
    # Return error is the item is not in the bag or any other exception occurs
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(content=e, status=400)
