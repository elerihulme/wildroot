from django.db import models
from django.templatetags.static import static
from cloudinary.models import CloudinaryField


class PlantCategory(models.Model):
    LIGHT_REQUIREMENTS = [
        ('low', 'Low Light'),
        ('medium', 'Medium Light'),
        ('high', 'High Light'),
    ]

    WATERING_FREQUENCY = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    CARING_DIFFICULTY = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    typical_light_requirements = models.CharField(
        max_length=10, choices=LIGHT_REQUIREMENTS, default='medium')
    typical_watering_frequency = models.CharField(
        max_length=10, choices=WATERING_FREQUENCY, default='medium')
    typical_caring_difficulty = models.CharField(
        max_length=10, choices=CARING_DIFFICULTY, default='medium')

    class Meta:
        verbose_name_plural = 'Plant Categories'

    def __str__(self):
        return self.name


class ShopPlant(models.Model):
    ENVIRONMENTS = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    ]

    category = models.ForeignKey(
        PlantCategory, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    botanical_name = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=50, blank=True)
    image = CloudinaryField('shop_plant_image', folder='shop_plant_images', blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_alt = models.CharField(max_length=255, blank=True)
    environment = models.CharField(
        max_length=10, choices=ENVIRONMENTS, default='indoor')
    pet_friendly = models.BooleanField(default=False)
    air_purifying = models.BooleanField(default=False)


    def get_image_url(self):
        if self.image:
            return self.image.url
        return static('images/placeholder.png')

    def __str__(self):
        return self.name