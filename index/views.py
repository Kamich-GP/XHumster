from django.shortcuts import render
from .models import Product, Category


# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД
    products = Product.objects.all()
    categories = Category.objects.all()

    # Передаем данные на фронт
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home.html', context)


# Страница в
