from django.urls import path
from .views import ProductDetailPage

urlpatterns = [
    path('product/<int:product_id>/detail', ProductDetailPage.as_view(), name='product_detail_page')
]