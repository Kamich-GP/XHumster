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


# Страница выбранной категории
def category_page(request, pk):
    # Достаем данные из БД
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(product_category=category)

    # Отправляем данные на фронт
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category.html', context)


# Страница выбранного товара
def product_page(request, pk):
    # Достаем данные из БД
    product = Product.objects.get(id=pk)

    # Передаем данные на фронт
    context = {'product': product}
    return render(request, 'product.html', context)


# Поиск товара
def search(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        searched_product = Product.objects.filter(product_name__iregex=get_product)

        if searched_product:
            context = {
                'products': searched_product,
                'request': get_product
            }
            return render(request, 'result.html', context)
        else:
            context = {
                'products': '',
                'request': get_product
            }
            return render(request, 'result.html', context)
