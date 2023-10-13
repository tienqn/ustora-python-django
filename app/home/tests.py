from django.test import TestCase
from slider.models import Slider
from product.models import Product
from product.models import ViewedProduct
from django.contrib.auth import get_user_model
import datetime
import pytz

class HomeTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username='root', email="normal@user.com", password="foo")

        Slider.objects.create(title='iPhone 6 Plus Dual SIM', url='img/h4-slide.png')
        Slider.objects.create(title='by one, get one 50% off school supplies & backpacks.*', url='img/h4-slide2.png')
        Slider.objects.create(title='Apple Store Ipod Select Item', url='img/h4-slide3.png')
        Slider.objects.create(title='Apple Store Ipod & Phone', url='img/h4-slide4.png')
        Slider.objects.create(title='Iphone15', url='img/h4-slide4.png')

        product01 = Product.objects.create(title='Samsung gallaxy note 4', img='img/product-6.jpg', origil_price=400, sell_price=400, sold_count=10)
        product02 = Product.objects.create(title='iPhone 6', img='img/product-5.jpg', origil_price=1355, sell_price=1200, sold_count=10)
        product03 = Product.objects.create(title='Sony microsoft', img='img/product-4.jpg', origil_price=225, sell_price=200, sold_count=120)
        product04 = Product.objects.create(title='LG Leon 2015', img='img/product-3.jpg', origil_price=425, sell_price=400, sold_count=10)
        product05 = Product.objects.create(title='Nokia Lumia 1320', img='img/product-2.jpg', origil_price=999, sell_price=899, sold_count=3)
        product06 = Product.objects.create(title='Samsung Galaxy s5- 2015', img='img/product-1.jpg', origil_price=700, sell_price=100, sold_count=70)

        view_time01 = datetime.datetime(2015, 10, 9, 23, 00, 59, 342380, tzinfo=pytz.UTC)
        view_time02 = datetime.datetime(2015, 10, 9, 23, 24, 59, 342380, tzinfo=pytz.UTC)
        view_time03 = datetime.datetime(2015, 10, 9, 23, 20, 59, 342380, tzinfo=pytz.UTC)
        view_time04 = datetime.datetime(2015, 10, 9, 23, 30, 59, 342380, tzinfo=pytz.UTC)
        view_time05 = datetime.datetime(2015, 10, 9, 23, 40, 59, 342380, tzinfo=pytz.UTC)
        ViewedProduct.objects.create(user_id=user, product_id=product01, view_time=view_time01)
        ViewedProduct.objects.create(user_id=user, product_id=product03, view_time=view_time02)
        ViewedProduct.objects.create(user_id=user, product_id=product02, view_time=view_time03)
        ViewedProduct.objects.create(user_id=user, product_id=product05, view_time=view_time04)
        ViewedProduct.objects.create(user_id=user, product_id=product01, view_time=view_time05)

    def test_can_access_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertEqual(len(response.context['slider_list']), 4)
        self.assertEqual(response.context['slider_list'][0].title, 'Iphone15')
        self.assertEqual(response.context['slider_list'][1].title, 'Apple Store Ipod & Phone')
        self.assertEqual(response.context['slider_list'][2].title, 'Apple Store Ipod Select Item')
        self.assertEqual(response.context['slider_list'][3].title, 'by one, get one 50% off school supplies & backpacks.*')
        self.assertEqual(len(response.context['latest_product']), 6)
        self.assertEqual(response.context['latest_product'][0].title, 'Samsung Galaxy s5- 2015')
        self.assertEqual(response.context['latest_product'][1].title, 'Nokia Lumia 1320')
        self.assertEqual(response.context['latest_product'][2].title, 'LG Leon 2015')
        self.assertEqual(response.context['latest_product'][3].title, 'Sony microsoft')
        self.assertEqual(response.context['latest_product'][4].title, 'iPhone 6')
        self.assertEqual(response.context['latest_product'][5].title, 'Samsung gallaxy note 4')
        self.assertEqual(len(response.context['top_sellers']), 3)
        self.assertEqual(response.context['top_sellers'][0].title, 'Sony microsoft')
        self.assertEqual(response.context['top_sellers'][1].title, 'Samsung Galaxy s5- 2015')
        self.assertEqual(response.context['top_sellers'][2].title, 'LG Leon 2015')
        self.assertEqual(len(response.context['recently_viewed']), 3)
        self.assertEqual(response.context['recently_viewed'][0].product_id.id, 1)
        self.assertEqual(response.context['recently_viewed'][1].product_id.id, 5)
        self.assertEqual(response.context['recently_viewed'][2].product_id.id, 3)
        self.assertEqual(len(response.context['top_new']), 3)
        self.assertEqual(response.context['top_new'][0].title, 'Samsung Galaxy s5- 2015')
        self.assertEqual(response.context['top_new'][1].title, 'Nokia Lumia 1320')
        self.assertEqual(response.context['top_new'][2].title, 'LG Leon 2015')