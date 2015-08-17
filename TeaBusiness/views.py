from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def index(request):
    return render_to_response('base.html',{})

def product_list(request):
    list_items = Products.objects.all()
    paginator = Paginator(list_items ,1)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)
    return render(request,'TeaBusiness/product_list.html',locals())

def product_detail(request, id):
    product_instance = Products.objects.get(id = id)
    return render(request,'TeaBusiness/view_product.html', locals())


