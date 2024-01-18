from django.shortcuts import get_object_or_404, render

from shop.models import Category, Product


# Create your views here.
def index(request):
    return render(request, 'shop/index.html', {
        'categories': Category.objects.all()})


def detail(request, product_id):
    return render(request, 'shop/detail.html', {
        'product': get_object_or_404(Product, id=product_id)})


def category(request, category_id):
    return render(request, 'shop/category.html', {
        'category': get_object_or_404(Category, id=category_id)})
