from django.urls import path
from .views import BusinessDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<str:url_identifier>/', BusinessDetailView.as_view(), name='business-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)