from django.test import TestCase
from slider.models import Slider

class HomeTestCase(TestCase):
    def setUp(self):
        Slider.objects.create(title='iPhone 6 Plus Dual SIM', url='img/h4-slide.png')
        Slider.objects.create(title='by one, get one 50% off school supplies & backpacks.*', url='img/h4-slide2.png')
        Slider.objects.create(title='Apple Store Ipod Select Item', url='img/h4-slide3.png')
        Slider.objects.create(title='Apple Store Ipod & Phone', url='img/h4-slide4.png')
        Slider.objects.create(title='Iphone15', url='img/h4-slide4.png')
    def test_can_access_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertEqual(len(response.context['slider_list']), 4)
        self.assertEqual(response.context['slider_list'][0].title, 'Iphone15')
        self.assertEqual(response.context['slider_list'][1].title, 'Apple Store Ipod & Phone')
        self.assertEqual(response.context['slider_list'][2].title, 'Apple Store Ipod Select Item')
        self.assertEqual(response.context['slider_list'][3].title, 'by one, get one 50% off school supplies & backpacks.*')