from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,ListView 
from .models import *
from django.urls import reverse
from .forms import AddToCartForm

class BusinessDetailView(DetailView):
    model = Business
    template_name = 'main/business_detail.html'
    context_object_name = 'business'

    def get_object(self):
        url_identifier = self.kwargs.get('url_identifier')
        return get_object_or_404(Business, url_identifier=url_identifier)

def item_detail(request, url_identifier, category_name, item_id):
    # Fetch the business, item, and category objects
    business = get_object_or_404(Business, url_identifier=url_identifier)
    item = get_object_or_404(Item, id=item_id)
    category = get_object_or_404(Category, business=business, name=category_name)

    # Render the template and pass the category
    return render(request, 'main/item_detail.html', {
        'business': business,
        'item': item,
        'category': category,
    })


class CategoryItemsView(ListView):
    model = Item
    template_name = 'main/category_items.html'
    context_object_name = 'items'

    def get_queryset(self):
        # Fetch business and category objects
        self.business = get_object_or_404(Business, url_identifier=self.kwargs['url_identifier'])
        self.category = get_object_or_404(Category, business=self.business, name=self.kwargs['category_name'])

        # Get all items in the category
        queryset = Item.objects.filter(category=self.category)

        # Apply filter based on the dropdown selection
        selected_filter = self.request.GET.get('filter')
        if selected_filter == 'sin_tacc':
            queryset = queryset.filter(sin_tacc=True)
        elif selected_filter == 'vegan':
            queryset = queryset.filter(vegan=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass business, category, and the full list of categories
        context['business'] = self.business
        context['category'] = self.category
        # Pass all categories belonging to the business for display purposes
        context['categories'] = Category.objects.filter(business=self.business)
        # Add the selected filter to the context
        context['selected_filter'] = self.request.GET.get('filter', '')
        return context