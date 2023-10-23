from django.views.generic.base import TemplateView
from .models import Product, ProductImage, ProductTag
from post.models import Post
from django.http import JsonResponse
import random

class ProductDetailPage(TemplateView):
    template_name = "product/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(pk=product_id)
        product_images = ProductImage.objects.filter(product_id=product_id).order_by('-id')

        product_tags_query = ProductTag.objects.filter(product=product)
        product_tags = [product_tag.tag for product_tag in product_tags_query]

        related_products = Product.objects.filter(category=product.category).exclude(id=product.id)

        all_products = Product.objects.all().exclude(id=product.id)
        random_products = random.sample(list(all_products), 4)
        recent_posts = Post.objects.all().order_by('-id')[:4]
        context["product"] = product
        context["product_images"] = product_images
        context["product_tags"] = product_tags
        context["related_products"] = related_products
        context["random_products"] = random_products
        context["recent_posts"] = recent_posts

        return context

def search_product(request):
    search_term = request.GET['q']
    filtered_products = Product.objects.filter(title__icontains=search_term)
    res = []
    for product in filtered_products:
        res.append({
            'id': product.id,
            'name': product.title,
        })
    return JsonResponse({'products':res})

