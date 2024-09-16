from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('business/<str:url_identifier>/', BusinessDetailView.as_view(), name='business-detail'),
    path('business/<str:url_identifier>/<str:category_name>/items/', CategoryItemsView.as_view(), name='category-items'),
    path('business/<str:url_identifier>/<str:category_name>/item/<int:item_id>/', item_detail, name='item-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
