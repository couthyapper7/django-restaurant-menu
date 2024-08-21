from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Business


class BusinessDetailView(DetailView):
    model = Business
    template_name = 'main/business_detail.html'
    context_object_name = 'business'

    def get_object(self):
        url_identifier = self.kwargs.get('url_identifier')
        return get_object_or_404(Business, url_identifier=url_identifier)
