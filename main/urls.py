from django.urls import path
from .views import BusinessDetailView

urlpatterns = [
    path('<str:url_identifier>/', BusinessDetailView.as_view(), name='business-detail'),
]