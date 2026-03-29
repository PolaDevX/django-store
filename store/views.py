from django.shortcuts import render
from . models import Product, Slider, Category
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    models = Product.objects.select_related('author').filter(featured=True)
    slides = Slider.objects.order_by('order')
    return render(request, 'index.html', {'products': models, 'slides': slides})


def product(request, pid):
    return render(
        request, 'product.html'
    )


def category(request, cid=None):
    cat = None
    cid = request.GET.get('cid')
    query = request.GET.get('query')
    where = {}

    if cid:
        cat = Category.objects.get(pk=cid)
        where['category_id'] = cid

    if query:
        where['name__icontains'] = query
            
    models = Product.objects.filter(**where)
    paginator = Paginator(models, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request, 'category.html', {'page_obj': page_obj, 'cat': cat}
    )


def cart(request):
    return render(
        request, 'cart.html'
    )


def checkout(request):
    return render(
        request, 'checkout.html'
    )


def checkout_complete(request):
    return render(
        request, 'checkout-complete.html'
    )