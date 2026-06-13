from django.shortcuts import render
from .models import Category, Product  # Підключаємо наші моделі баз даних


def home_view(request):
    # Дістаємо всі категорії з бази даних для меню
    categories = Category.objects.all()

    # Логіка вибору категорії з меню
    category_id = request.GET.get('category')
    if category_id:
        # Якщо користувач натиснув на категорію, показуємо товари тільки з неї
        products = Product.objects.filter(category_id=category_id)
    else:
        # Якщо нічого не вибрано, показуємо всі товари
        products = Product.objects.all()

    context = {
        'title': 'Головна сторінка',
        'is_home': True,
        'categories': categories,
        'products': products,
    }
    return render(request, 'pages/page.html', context)


def about_view(request):
    context = {
        'title': 'Про нас',
        'content': 'Це сторінка про наш магазин. Ми продаємо найкращі меблі.',
        'is_home': False,
    }
    return render(request, 'pages/page.html', context)


def contacts_view(request):
    context = {
        'title': 'Контакти',
        'content': 'Зв\'яжіться з нами за телефоном: +38000000000',
        'is_home': False,
    }
    return render(request, 'pages/page.html', context)