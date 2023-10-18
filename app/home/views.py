from django.views.generic.base import TemplateView
from slider.models import Slider
from product.models import Product, ViewedProduct, ProductImage


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider_list = Slider.objects.order_by('-id').all()[:4]
        latest_product = Product.objects.order_by('-id').all()[:6]
        product_list = []
        for product in latest_product:
            product_images = ProductImage.objects.filter(product=product)
            main_image = product_images.filter(is_main_image=True).first()
            if main_image is None:
                img = ''
            else:
                img = main_image.image
            product_dict = {
                'id': product.id,
                'title': product.title,
                'origil_price': product.origil_price,
                'sell_price': product.sell_price,
                'sold_count': product.sold_count,
                'added_time': product.added_time,
                'image': img,
            }
            product_list.append(product_dict)
        top_sellers = Product.objects.order_by('-sold_count', '-id').all()[:3]
        recently_viewed = ViewedProduct.objects.order_by('-view_time').all()[:3]
        top_new = Product.objects.order_by('-added_time').all()[:3]
        context["name"] = "world"
        context["slider_list"] = slider_list
        context["latest_product"] = product_list
        context["top_sellers"] = top_sellers
        context["recently_viewed"] = recently_viewed
        context["top_new"] = top_new
        return context