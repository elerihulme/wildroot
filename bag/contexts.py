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

    for item_id, quantity in list(bag.items()):
        try:
            plant = ShopPlant.objects.get(id=item_id)
        except ShopPlant.DoesNotExist:
            bag.pop(item_id)
            continue
        total += quantity * plant.price
        plant_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'plant': plant,
            'item_total': quantity * plant.price,
        })

    request.session['bag'] = bag

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
