from django.views.generic import ListView
from django.shortcuts import render
from .models import ShopPlant, PlantCategory

class ProductList(ListView):
    model = ShopPlant
    template_name = 'products/product_list.html'
    context_object_name = 'plants'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category', None)
        environment = self.request.GET.get('environment', None)

        if category:
            queryset = queryset.filter(category__name__iexact=category)
        if environment:
            queryset = queryset.filter(environment=environment)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PlantCategory.objects.all()
        return context

