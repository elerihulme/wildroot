from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class UserPlant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_plants')
    plant_species = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    last_watered = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nickname} ({self.plant_species})"

    def get_latest_image_url(self):
        latest_photo = self.photos.order_by('-timestamp').first()
        if latest_photo and latest_photo.image:
            return latest_photo.image.url
        return static('images/placeholder.png')

    def get_all_photos(self):
        return self.photos.order_by('timestamp')

class UserPlantPhoto(models.Model):
    user_plant = models.ForeignKey(UserPlant, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='user_plant_photos/')
    caption = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image_alt = models.CharField(max_length=255, blank=False)

    def image_url(self):
        if self.image:
            return self.image.url
        return static('images/placeholder.png')

    def __str__(self):
        return f"Photo of {self.user_plant.nickname} at {self.timestamp}"
