from django.test import TestCase
from slider.models import Slider
from product.models import Product,ViewedProduct,ProductImage, ProductCategory, Tag, ProductTag
from post.models import Post
from django.contrib.auth import get_user_model
import datetime
import pytz
from django.urls import reverse

class HomeTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='root', email="normal@user.com", password="foo")

        self.slider01 = Slider.objects.create(title='iPhone 6 Plus Dual SIM', url='img/h4-slide.png')
        self.slider02 = Slider.objects.create(title='by one, get one 50% off school supplies & backpacks.*', url='img/h4-slide2.png')
        self.slider03 = Slider.objects.create(title='Apple Store Ipod Select Item', url='img/h4-slide3.png')
        self.slider04 = Slider.objects.create(title='Apple Store Ipod & Phone', url='img/h4-slide4.png')
        self.slider05 = Slider.objects.create(title='Iphone15', url='img/h4-slide4.png')

        self.product01 = Product.objects.create(title='Samsung gallaxy note 4', origil_price=400, sell_price=400, sold_count=10)
        self.product_image01_01 = ProductImage.objects.create(product=self.product01, image=f'example_image_1.jpg', is_main_image=True,)
        self.product_image01_02 = ProductImage.objects.create(product=self.product01, image=f'example_image_2.jpg', is_main_image=False,)
        self.product_image01_03 = ProductImage.objects.create(product=self.product01, image=f'example_image_3.jpg', is_main_image=False,)

        self.product02 = Product.objects.create(title='iPhone 6', origil_price=1355, sell_price=1200, sold_count=10)
        self.product_image02_01 = ProductImage.objects.create(product=self.product02, image=f'example_image_1.jpg', is_main_image=False,)
        self.product_image02_02 = ProductImage.objects.create(product=self.product02, image=f'example_image_2.jpg', is_main_image=True,)
        self.product_image02_03 = ProductImage.objects.create(product=self.product02, image=f'example_image_3.jpg', is_main_image=False,)

        self.product03 = Product.objects.create(title='Sony microsoft', origil_price=225, sell_price=200, sold_count=120)
        self.product_image03_01 = ProductImage.objects.create(product=self.product03, image=f'example_image_1.jpg', is_main_image=True,)
        self.product_image03_02 = ProductImage.objects.create(product=self.product03, image=f'example_image_2.jpg', is_main_image=False,)
        self.product_image03_03 = ProductImage.objects.create(product=self.product03, image=f'example_image_3.jpg', is_main_image=False,)

        self.product04 = Product.objects.create(title='LG Leon 2015', origil_price=425, sell_price=400, sold_count=10)
        self.product_image04_01 = ProductImage.objects.create(product=self.product04, image=f'example_image_1.jpg', is_main_image=True,)
        self.product_image04_02 = ProductImage.objects.create(product=self.product04, image=f'example_image_2.jpg', is_main_image=False,)
        self.product_image04_03 = ProductImage.objects.create(product=self.product04, image=f'example_image_3.jpg', is_main_image=False,)

        self.product05 = Product.objects.create(title='Nokia Lumia 1320', origil_price=999, sell_price=899, sold_count=3)
        self.product_image05_01 = ProductImage.objects.create(product=self.product05, image=f'example_image_1.jpg', is_main_image=True,)
        self.product_image05_02 = ProductImage.objects.create(product=self.product05, image=f'example_image_2.jpg', is_main_image=False,)
        self.product_image05_03 = ProductImage.objects.create(product=self.product05, image=f'example_image_3.jpg', is_main_image=False,)

        self.product06 = Product.objects.create(title='Samsung Galaxy s5- 2015', origil_price=700, sell_price=100, sold_count=70)
        self.product_image06_01 = ProductImage.objects.create(product=self.product06, image=f'example_image_1.jpg', is_main_image=True,)
        self.product_image06_02 = ProductImage.objects.create(product=self.product06, image=f'example_image_2.jpg', is_main_image=False,)
        self.product_image06_03 = ProductImage.objects.create(product=self.product06, image=f'example_image_3.jpg', is_main_image=False,)

        view_time01 = datetime.datetime(2015, 10, 9, 23, 00, 59, 342380, tzinfo=pytz.UTC)
        view_time02 = datetime.datetime(2015, 10, 9, 23, 24, 59, 342380, tzinfo=pytz.UTC)
        view_time03 = datetime.datetime(2015, 10, 9, 23, 20, 59, 342380, tzinfo=pytz.UTC)
        view_time04 = datetime.datetime(2015, 10, 9, 23, 30, 59, 342380, tzinfo=pytz.UTC)
        view_time05 = datetime.datetime(2015, 10, 9, 23, 40, 59, 342380, tzinfo=pytz.UTC)
        ViewedProduct.objects.create(user_id=self.user, product_id=self.product01, view_time=view_time01)
        ViewedProduct.objects.create(user_id=self.user, product_id=self.product03, view_time=view_time02)
        ViewedProduct.objects.create(user_id=self.user, product_id=self.product02, view_time=view_time03)
        ViewedProduct.objects.create(user_id=self.user, product_id=self.product05, view_time=view_time04)
        ViewedProduct.objects.create(user_id=self.user, product_id=self.product01, view_time=view_time05)

    def test_can_access_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertEqual(len(response.context['slider_list']), 4)
        self.assertEqual(response.context['slider_list'][0].title, self.slider05.title)
        self.assertEqual(response.context['slider_list'][1].title, self.slider04.title)
        self.assertEqual(response.context['slider_list'][2].title, self.slider03.title)
        self.assertEqual(response.context['slider_list'][3].title, self.slider02.title)
        self.assertEqual(len(response.context['latest_product']), 6)
        self.assertEqual(response.context['latest_product'][0]['title'], self.product06.title)
        self.assertEqual(response.context['latest_product'][0]['image'], self.product_image06_01.image)
        self.assertEqual(response.context['latest_product'][1]['title'], self.product05.title)
        self.assertEqual(response.context['latest_product'][1]['image'], self.product_image05_01.image)
        self.assertEqual(response.context['latest_product'][2]['title'], self.product04.title)
        self.assertEqual(response.context['latest_product'][2]['image'], self.product_image04_01.image)
        self.assertEqual(response.context['latest_product'][3]['title'], self.product03.title)
        self.assertEqual(response.context['latest_product'][3]['image'], self.product_image03_01.image)
        self.assertEqual(response.context['latest_product'][4]['title'], self.product02.title)
        self.assertEqual(response.context['latest_product'][4]['image'], self.product_image02_02.image)
        self.assertEqual(response.context['latest_product'][5]['title'], self.product01.title)
        self.assertEqual(response.context['latest_product'][5]['image'], self.product_image01_01.image)
        self.assertEqual(len(response.context['top_sellers']), 3)
        self.assertEqual(response.context['top_sellers'][0].title, self.product03.title)
        self.assertEqual(response.context['top_sellers'][1].title, self.product06.title)
        self.assertEqual(response.context['top_sellers'][2].title, self.product04.title)
        self.assertEqual(len(response.context['recently_viewed']), 3)
        self.assertEqual(response.context['recently_viewed'][0].product_id.title, self.product01.title)
        self.assertEqual(response.context['recently_viewed'][1].product_id.title, self.product05.title)
        self.assertEqual(response.context['recently_viewed'][2].product_id.title, self.product03.title)
        self.assertEqual(len(response.context['top_new']), 3)
        self.assertEqual(response.context['top_new'][0].title, self.product06.title)
        self.assertEqual(response.context['top_new'][1].title, self.product05.title)
        self.assertEqual(response.context['top_new'][2].title, self.product04.title)

class CartTest(TestCase):
    def setUp(self):
        self.product01 = Product.objects.create(title='Samsung gallaxy note 4', origil_price=400, sell_price=400, sold_count=10)
        self.product02 = Product.objects.create(title='iPhone 6', origil_price=1355, sell_price=1200, sold_count=10)
        self.product01_id = str(self.product01.id)
        self.product02_id = str(self.product02.id)

    def test_add_to_cart(self):
        response = self.client.get('/')
        cart = response.client.session.get('cart', {})
        self.assertEqual(cart, {})
        
        response = self.client.post(reverse('add_to_cart', args=[self.product01.id]))
        self.assertEqual(response.status_code, 200)
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[self.product01_id]['product']['title'], self.product01.title)
        self.assertEqual(cart[self.product01_id]['quantity'], 1)

        response = self.client.post(reverse('add_to_cart', args=[self.product01.id]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('add_to_cart', args=[self.product01.id]))
        self.assertEqual(response.status_code, 200)
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[self.product01_id]['quantity'], 3)
        
        response = self.client.post(reverse('add_to_cart', args=[self.product02.id]))
        self.assertEqual(response.status_code, 200)
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[self.product01_id]['product']['title'], self.product01.title)
        self.assertEqual(cart[self.product02_id]['product']['title'], self.product02.title)
        self.assertEqual(len(cart), 2)

class ProductDetailTest(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(title="category 01")
        self.category02 = ProductCategory.objects.create(title="category 02")
        self.product = Product.objects.create(title='Samsung gallaxy note 4', description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tristique, diam in consequat iaculis, est purus iaculis mauris, imperdiet facilisis ante ligula at nulla.", origil_price=400, sell_price=400, sold_count=10, category=self.category)
        self.product_image01 = ProductImage.objects.create(product=self.product, image=f'example_image_1.jpg', is_main_image=True,)
        self.product_image02 = ProductImage.objects.create(product=self.product, image=f'example_image_2.jpg', is_main_image=False,)
        self.product_image03 = ProductImage.objects.create(product=self.product, image=f'example_image_3.jpg', is_main_image=False,)

        self.product02 = Product.objects.create(title='Samsung gallaxy note 5', description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tristique, diam in consequat iaculis, est purus iaculis mauris, imperdiet facilisis ante ligula at nulla.", origil_price=400, sell_price=400, sold_count=10, category=self.category02)
        self.product02_image01 = ProductImage.objects.create(product=self.product02, image=f'example_image_1.jpg', is_main_image=True,)
        self.product02_image02 = ProductImage.objects.create(product=self.product02, image=f'example_image_2.jpg', is_main_image=False,)
        self.product02_image03 = ProductImage.objects.create(product=self.product02, image=f'example_image_3.jpg', is_main_image=False,)

        self.product03 = Product.objects.create(title='Samsung gallaxy note 6', description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tristique, diam in consequat iaculis, est purus iaculis mauris, imperdiet facilisis ante ligula at nulla.", origil_price=400, sell_price=400, sold_count=10, category=self.category)
        self.product03_image01 = ProductImage.objects.create(product=self.product03, image=f'example_image_1.jpg', is_main_image=True,)
        self.product03_image02 = ProductImage.objects.create(product=self.product03, image=f'example_image_2.jpg', is_main_image=False,)
        self.product03_image03 = ProductImage.objects.create(product=self.product03, image=f'example_image_3.jpg', is_main_image=False,)

        self.product04 = Product.objects.create(title='Samsung gallaxy note 7', description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tristique, diam in consequat iaculis, est purus iaculis mauris, imperdiet facilisis ante ligula at nulla.", origil_price=400, sell_price=400, sold_count=10, category=self.category)
        self.product04_image01 = ProductImage.objects.create(product=self.product04, image=f'example_image_1.jpg', is_main_image=True,)
        self.product04_image02 = ProductImage.objects.create(product=self.product04, image=f'example_image_2.jpg', is_main_image=False,)
        self.product04_image03 = ProductImage.objects.create(product=self.product04, image=f'example_image_3.jpg', is_main_image=False,)

        self.product05 = Product.objects.create(title='Samsung gallaxy note 8', description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tristique, diam in consequat iaculis, est purus iaculis mauris, imperdiet facilisis ante ligula at nulla.", origil_price=400, sell_price=400, sold_count=10, category=self.category)
        self.product05_image01 = ProductImage.objects.create(product=self.product05, image=f'example_image_1.jpg', is_main_image=True,)
        self.product05_image02 = ProductImage.objects.create(product=self.product05, image=f'example_image_2.jpg', is_main_image=False,)
        self.product05_image03 = ProductImage.objects.create(product=self.product05, image=f'example_image_3.jpg', is_main_image=False,)

        self.tag01 = Tag.objects.create(name="tag01")
        self.tag02 = Tag.objects.create(name="tag02")
        self.tag03 = Tag.objects.create(name="tag03")

        ProductTag.objects.create(tag=self.tag01, product=self.product)
        ProductTag.objects.create(tag=self.tag02, product=self.product)
        ProductTag.objects.create(tag=self.tag03, product=self.product)

        self.post01 = Post.objects.create(title="post1", content="content01")
        self.post02 = Post.objects.create(title="post2", content="content02")
        self.post03 = Post.objects.create(title="post3", content="content03")
        self.post04 = Post.objects.create(title="post4", content="content04")
        self.post05 = Post.objects.create(title="post5", content="content05")

    def test_can_access_detail_page(self):
        response = self.client.get(reverse('product_detail_page', args=[self.product.id]))
        self.assertTemplateUsed('product/detail.html')
        self.assertEqual(response.context['product'].title, self.product.title)
        self.assertEqual(response.context['product'].description, self.product.description)
        self.assertEqual(response.context['product'].category.title, self.product.category.title)
        self.assertEqual(len(response.context['product_tags']), 3)
        self.assertEqual(response.context['product_tags'][0].name, self.tag01.name)
        self.assertEqual(response.context['product_tags'][1].name, self.tag02.name)
        self.assertEqual(response.context['product_tags'][2].name, self.tag03.name)
        self.assertEqual(len(response.context['product_images']), 3)
        self.assertEqual(response.context['product_images'][2].image, self.product_image01.image)
        self.assertEqual(response.context['product_images'][2].is_main_image, self.product_image01.is_main_image)
        self.assertEqual(len(response.context['related_products']), 3)
        self.assertEqual(response.context['related_products'][0].title, self.product03.title)
        self.assertEqual(response.context['related_products'][1].title, self.product04.title)
        self.assertEqual(response.context['related_products'][2].title, self.product05.title)
        self.assertEqual(len(response.context['random_products']), 4)
        self.assertEqual(len(response.context['recent_posts']), 4)
        self.assertEqual(response.status_code, 200)
        