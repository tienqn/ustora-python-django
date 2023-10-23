from django.urls import path
from .views import HomePageView, subcribe

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('subcribe', subcribe, name="subcribe"),
]