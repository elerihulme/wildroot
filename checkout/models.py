import uuid
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from products.models import ShopPlant

# UK Postcode Validator
uk_postcode_validator = RegexValidator(
    regex=r"^(GIR ?0AA|[A-PR-UWYZ][0-9][0-9]? ?[0-9][ABD-HJLNP-UW-Z]{2}|[A-PR-UWYZ][A-HK-Y][0-9][0-9]? ?[0-9][ABD-HJLNP-UW-Z]{2}|[A-PR-UWYZ][0-9][A-HJKSTUW]? ?[0-9][ABD-HJLNP-UW-Z]{2}|[A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]? ?[0-9][ABD-HJLNP-UW-Z]{2})$",
    message="Enter a valid UK postcode."
)

# Country choices
COUNTRY_CHOICES = [
    ('GB', 'United Kingdom'),
]

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[uk_postcode_validator]
    )
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(
        max_length=40,
        choices=COUNTRY_CHOICES,
        default='GB',
        null=False,
        blank=False
    )
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override save to set the order number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='items')
    plant = models.ForeignKey(ShopPlant, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override save to set item total based on plant price and quantity.
        """
        self.item_total = self.plant.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.plant.name} on order {self.order.order_number}'
