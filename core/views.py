from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from core.models import Product


def index(request):
    produtos = Product.objects.all()
    context = {
        'curso': 'Programação web com django framework.',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, product_id):
    # prod = Product.objects.get(id=product_id)
    prod = get_object_or_404(Product, id=product_id)
    context = {
        'name': prod.name,
        'price': prod.price,
        'quantity': prod.quantity,
    }
    return render(request, 'product.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
