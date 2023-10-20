from django.urls import path
from .views import ProductDetailPage,search_product

urlpatterns = [
    path('product/<int:product_id>/detail', ProductDetailPage.as_view(), name='product_detail_page'),
    path('product/search', search_product, name='product_search_page'),
]