from django.views.generic.base import TemplateView

from .models import Product, ProductImage

class ProductDetailPage(TemplateView):
    template_name = "product/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(pk=product_id)
        product_images = ProductImage.objects.filter(product_id=product_id)
        context["product"] = product
        context["product_images"] = product_images
        return context
