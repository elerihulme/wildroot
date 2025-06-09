from decimal import Decimal
from django.conf import settings
from products.models import ShopPlant

def bag_contents(request):
    """
    Make the bag available in all templates
    """
    bag_items = []
    total = 0
    plant_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        plant = ShopPlant.objects.get(id=item_id)
        total += quantity * plant.price
        plant_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'plant': plant,
            'item_total': quantity * plant.price,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'plant_count': plant_count,
    }

    return context