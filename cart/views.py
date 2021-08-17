from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm



def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.GET)
    

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    else:
        cd = form.cleaned_data
        cart.add(product=product, quantity=1, update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, 'Удалено')
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)


    categories = Category.objects.all()
    carts = Cart(request)

    list_categories_8=categories
    list_categories_8 = [categories[d:d+8] for d in range(0, len(list_categories_8), 8)]
    categories_navbar1=list_categories_8[0]

    categories_navbar2=[]
    categories_navbar3=[]
    categories_navbar4=[]
    if len(categories)>8:
        categories_navbar2=list_categories_8[1]
    if len(categories)>16:
        categories_navbar3=list_categories_8[1]
    if len(categories)>24:
        categories_navbar4=list_categories_8[1]

    list_categories_footer_6=categories

    list_categories_footer_6=[categories[d:d+8]
                     for d in range(0, len(list_categories_footer_6), 6)]
    categories_footer1 = list_categories_footer_6[0]

    categories_footer2=[]
    categories_footer3=[]
    categories_footer4=[]
    categories_footer5=[]


    if len(categories)>6:
        categories_footer2=list_categories_footer_6[1]
    if len(categories)>16:
        categories_footer3=list_categories_footer_6[2]
    if len(categories)>24:
        categories_footer4=list_categories_footer_6[3]
    if len(categories)>30:
        categories_footer5=list_categories_footer_6[4]


    context = {
        
        'categories': categories,
        'categories_footer1': categories_footer1,
        'categories_footer2': categories_footer2,
        'categories_footer3': categories_footer3,
        'categories_footer4': categories_footer4,
        'categories_footer5': categories_footer5,
        'categories_navbar1': categories_navbar1,
        'categories_navbar2': categories_navbar2,
        'categories_navbar3': categories_navbar3,
        'categories_navbar4': categories_navbar4,
        'cart': cart

    }
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', context)