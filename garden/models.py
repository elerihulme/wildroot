from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from cloudinary.models import CloudinaryField

class UserPlant(models.Model):
    """
    Model to represent a user's plant in their personal garden.
    Each user can have multiple plants, and each plant can have multiple photos.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_plants')
    plant_species = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    last_watered = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nickname} ({self.plant_species})"

    def get_latest_image_url(self):
        """
        Return the URL of the most recently added photo for this plant.
        If no photos are available, return the path to a placeholder image.
        """
        latest_photo = self.photos.order_by('-timestamp').first()
        if latest_photo and latest_photo.image:
            return latest_photo.image.url
        return static('images/placeholder.png')

    def get_all_photos(self):
        """ Return all photos associated with this plant, ordered by timestamp. """
        return self.photos.order_by('timestamp')

class UserPlantPhoto(models.Model):
    """
    Model to represent a photo of a user's plant.
    Each photo is associated with a specific UserPlant.
    """
    user_plant = models.ForeignKey(UserPlant, on_delete=models.CASCADE, related_name='photos')
    image = CloudinaryField('user_plant_image', folder='user_plant_photos', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image_alt = models.CharField(max_length=255, blank=False)

    def image_url(self):
        """
        Return the URL of the uploaded image.
        If no image is uploaded, return the path to a placeholder image.
        """
        if self.image:
            return self.image.url
        return static('images/placeholder.png')

    def __str__(self):
        return f"Photo of {self.user_plant.nickname} at {self.timestamp}"
