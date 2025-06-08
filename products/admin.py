from django.contrib import admin

from .models import PlantCategory, ShopPlant

class PlantCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'typical_light_requirements', 'typical_watering_frequency', 'typical_caring_difficulty')

class ShopPlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'environment', 'pet_friendly', 'air_purifying')
    search_fields = ('name', 'botanical_name', 'description')
    list_filter = ('category', 'environment', 'pet_friendly', 'air_purifying')

admin.site.register(PlantCategory, PlantCategoryAdmin)
admin.site.register(ShopPlant, ShopPlantAdmin)