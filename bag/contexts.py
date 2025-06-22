from decimal import Decimal
from products.models import ShopPlant


def bag_contents(request):
    """
    Make the bag available in all templates
    """
    bag_items = []
    total = 0
    plant_count = 0
    bag = request.session.get('bag', {})

    # Iterate through the bag items and calculate totals
    for item_id, quantity in list(bag.items()):
        # Try to get the plant object, if it doesn't exist,
        # remove it from the bag
        try:
            plant = ShopPlant.objects.get(id=item_id)
        except ShopPlant.DoesNotExist:
            bag.pop(item_id)
            continue
        # Calculate the total price and plant count
        total += quantity * plant.price
        plant_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'plant': plant,
            'item_total': quantity * plant.price,
        })

    # Update the session bag with the current state
    request.session['bag'] = bag

    # Calculate delivery and grand total
    delivery = Decimal('5.00')
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'plant_count': plant_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
