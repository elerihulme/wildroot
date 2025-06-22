from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import ShopPlant, PlantCategory
from django.contrib import messages
from urllib.parse import urlencode

class ProductList(ListView):
    """ View to list all plants with filtering and sorting options. """
    model = ShopPlant
    template_name = 'products/product_list.html'
    context_object_name = 'plants'
    paginate_by = 12

    # Override the get_queryset method to apply filters and sorting
    def get_queryset(self):
        queryset = super().get_queryset()

        # Filters
        environment = self.request.GET.get('environment')
        category = self.request.GET.get('category')
        difficulty = self.request.GET.get('difficulty')
        pet_friendly = self.request.GET.get('pet_friendly')
        air_purifying = self.request.GET.get('air_purifying')
        shade_tolerant = self.request.GET.get('shade_tolerant') 
        sort_by = self.request.GET.get('sort')

        # Apply filters
        if environment:
            queryset = queryset.filter(environment=environment)
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        if difficulty:
            queryset = queryset.filter(category__typical_caring_difficulty=difficulty)
        if pet_friendly == 'true':
            queryset = queryset.filter(pet_friendly=True)
        if air_purifying == 'true':
            queryset = queryset.filter(air_purifying=True)
        if shade_tolerant == 'true':
            queryset = queryset.filter(category__typical_light_requirements='low')

        # Sorting
        if sort_by == 'price_low':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_high':
            queryset = queryset.order_by('-price')

        return queryset


    def get_context_data(self, **kwargs):
        """ Add additional context data for the template. """
        context = super().get_context_data(**kwargs)
        # Add categories to the context
        context['categories'] = PlantCategory.objects.all()
        # Add the current filters to the context, exluding pagination
        querystring = self.request.GET.copy()
        if 'page' in querystring:
            querystring.pop('page')
        # Add the current querystring to the context for filtering and sorting links
        context['querystring'] = querystring.urlencode()
        return context

def product_detail(request, pk):
    """ View to display detailed information about a specific plant. """
    plant = get_object_or_404(ShopPlant, pk=pk)
    querystring = request.GET.urlencode()
    context = {
        'plant': plant,
        'querystring': querystring,
    }
    return render(request, 'products/product_detail.html', context)