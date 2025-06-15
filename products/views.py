from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import ShopPlant, PlantCategory

class ProductList(ListView):
    model = ShopPlant
    template_name = 'products/product_list.html'
    context_object_name = 'plants'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filters
        category = self.request.GET.get('category')
        difficulty = self.request.GET.get('difficulty')
        pet_friendly = self.request.GET.get('pet_friendly')
        air_purifying = self.request.GET.get('air_purifying')
        shade_tolerant = self.request.GET.get('shade_tolerant')  # Assuming you’ve added this boolean field
        sort_by = self.request.GET.get('sort')

        if category:
            queryset = queryset.filter(category__name__iexact=category)
        if difficulty:
            queryset = queryset.filter(category__typical_caring_difficulty=difficulty)
        if pet_friendly == 'true':
            queryset = queryset.filter(pet_friendly=True)
        if air_purifying == 'true':
            queryset = queryset.filter(air_purifying=True)
        if shade_tolerant == 'true':
            queryset = queryset.filter(category__typical_light_requirements='low')  # assuming low light = shade

        # Sorting
        if sort_by == 'price_low':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_high':
            queryset = queryset.order_by('-price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PlantCategory.objects.all()
        return context

def product_detail(request, pk):
    plant = get_object_or_404(ShopPlant, pk=pk)
    return render(request, 'products/product_detail.html', {'plant': plant})