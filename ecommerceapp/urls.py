from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('checkout/',views.checkout,name="checkout"),
    
    # path('handlerequest/',views.handlerequest,name="HandleRequest"),
]
