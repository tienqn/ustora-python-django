from django.views.generic.base import TemplateView
from slider.models import Slider


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider_list = Slider.objects.order_by('-id').all()[:4]
        context["name"] = "world"
        context["slider_list"] = slider_list
        return context