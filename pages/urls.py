from django.urls import path
from .views import home, clothes , accesorries, mobiles, electronics, clothes_detail

urlpatterns = [
    path('', home, name='home'),
    path('clothes/', clothes, name='clothes'),
    path('clothes/<pk>/', clothes_detail, name='clothes_detail'),
    path('accessories/', accesorries, name='accessories'),
    path('mobiles/', mobiles, name='mobiles'),
    path('electronics/', electronics, name='electronics'),

]