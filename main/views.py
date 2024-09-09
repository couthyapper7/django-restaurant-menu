from django.shortcuts import get_object_or_404
from django.views.generic import DetailView,ListView 
from .models import *


class BusinessDetailView(DetailView):
    model = Business
    template_name = 'main/business_detail.html'
    context_object_name = 'business'

    def get_object(self):
        url_identifier = self.kwargs.get('url_identifier')
        return get_object_or_404(Business, url_identifier=url_identifier)

class CategoryItemsView(ListView):
    model = Item
    template_name = 'main/category_items.html'
    context_object_name = 'items'

    def get_queryset(self):
        self.business = get_object_or_404(Business, url_identifier=self.kwargs['url_identifier'])
        self.category = get_object_or_404(Category, business=self.business, name=self.kwargs['category_name'])
        return Item.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business'] = self.business
        context['categories'] = self.get_queryset()  # Ensuring categories are passed
        return context

class BusinessCategoriesView(ListView):
    model = Category
    template_name = 'main/business_categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        self.business = get_object_or_404(Business, url_identifier=self.kwargs['url_identifier'])
        return Category.objects.filter(business=self.business)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business'] = self.business
        return context
