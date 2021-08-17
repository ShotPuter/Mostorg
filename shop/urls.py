from django.contrib import admin
from django.urls import path

from shop.views import (
    product_list, 
    product_detail,
    start_page,
    
)
from shop.views import contact, about, make_callback
app_name = 'shop'

urlpatterns = [
    path('', start_page, name='start_page'),

    path('catalog/', product_list, name='product_list'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),   
    path('<str:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<str:slug>/', product_detail, name='product_detail'),
    path('make-callback/new/', make_callback, name='callback')
   
]
