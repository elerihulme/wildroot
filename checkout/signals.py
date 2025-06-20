from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem

# Signal to update the order total whenever an OrderItem is created or updated
@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()

# Signal to update the order total whenever an OrderItem is deleted
@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()