from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product, Callback
from cart.forms import CartAddProductForm
from .forms import CallbackForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView
)
from cart.cart import Cart

'''
class ProductListView(ListView):
    template_name = 'shop/product/list.html'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
'''

def start_page(request):
    products = Product.objects.filter(available=True)
    last_products = Product.objects.filter(available=True)[:8]
    categories = Category.objects.all()
    carts = Cart(request)

    categories_len=len(categories)
    

    
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
        'products': products,
        'last_products': last_products,
        'categories': categories,
        'categories_navbar1': categories_navbar1,
        'categories_navbar2': categories_navbar2,
        'categories_navbar3': categories_navbar3,
        'categories_navbar4': categories_navbar4,
        'categories_footer1': categories_footer1,
        'categories_footer2': categories_footer2,
        'categories_footer3': categories_footer3,
        'categories_footer4': categories_footer4,
        'categories_footer5': categories_footer5


    }
    return render(request, 'start.html', context)

    
def contact(request):
   
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



    }
     
    return render(request, 'contact.html', context)
        


def about(request):
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


    }




    return render(request, 'about.html', context)

def product_list(request, category_slug=None, all=None, price_low=None, price_height=None, rathings_low=None, rathings_height=None):

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    categories_len=len(categories)

    if request.GET.get('price_low'):
        products=products.order_by("price")
    if request.GET.get('price_height'):
        products=products.order_by("price").reverse()
    if request.GET.get('rathins_height'):
        products=products.order_by("degree").reverse()
    if request.GET.get('rathins_low'):
        products=products.order_by("degree")

    
    list_categories_8 = categories
    list_categories_8 = [categories[d:d+8]
                     for d in range(0, len(list_categories_8), 8)]
    categories_navbar1 = list_categories_8[0]


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

    paginator = Paginator(products, 9)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products= paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
       products = paginator.page(paginator.num_pages) # Show 25 contacts per page
   





    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'categories_navbar1': categories_navbar1,
        'categories_navbar2': categories_navbar2,
        'categories_navbar3': categories_navbar3,
        'categories_navbar4': categories_navbar4,
        'categories_footer1': categories_footer1,
        'categories_footer2': categories_footer2,
        'categories_footer3': categories_footer3,
        'categories_footer4': categories_footer4,
        'categories_footer5': categories_footer5
    }
    return render(request, 'catalog.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

@csrf_exempt
def make_callback(request):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            description = form.cleaned_data['description']
            Callback(name=name,phone=phone,description=description).save()
            messages.success(request, 'Спасибо, мы перезвоним Вам!')
            redirect('/contact/')
    
    return redirect('/contact/')

