from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Category, Product, Rating, Subscriber, Order
from .forms import UserRegisterForm


# --- Головні сторінки ---
def home_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cart_count = len(request.session.get('cart', []))
    return render(request, 'pages/page.html', {
        'title': 'StalLine - Каталог продукції',
        'is_home': True,
        'categories': categories,
        'products': products,
        'cart_count': cart_count
    })


def about_view(request):
    content = '''Компанія StalLine — це преміальна якість та надійність у кожній деталі.
    Ми створюємо унікальні вироби, поєднуючи класичні традиції обробки металу та дерева з сучасним дизайном. 
    Обираючи StalLine, ви обираєте довговічність та бездоганний стиль для вашого простору.'''
    return render(request, 'pages/page.html', {
        'title': 'Про компанію StalLine',
        'content': content,
        'cart_count': len(request.session.get('cart', []))
    })


def contacts_view(request):
    content = '''Зв'яжіться з менеджером StalLine для консультації або індивідуального замовлення.
    Телефон: +380981771025
    Email: neblivolyn@gmail.com'''
    return render(request, 'pages/page.html', {
        'title': 'Контакти StalLine',
        'content': content,
        'cart_count': len(request.session.get('cart', []))
    })


# --- Каталог ---
def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'pages/category.html', {
        'title': f'StalLine: {category.name}',
        'category': category,
        'products': products,
        'categories': categories,
        'is_home': True,
        'cart_count': len(request.session.get('cart', []))
    })


def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST' and 'rating' in request.POST:
        Rating.objects.create(product=product, score=int(request.POST.get('rating')))
        return redirect('product', product_id=product.id)

    ratings = product.ratings.all()
    avg_rating = sum(r.score for r in ratings) / ratings.count() if ratings.count() > 0 else 0
    return render(request, 'pages/product.html', {
        'title': product.title,
        'product': product,
        'avg_rating': round(avg_rating, 1),
        'cart_count': len(request.session.get('cart', []))
    })


# --- Кошик та Замовлення ---
def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        cart.append(product_id)
        request.session['cart'] = cart
    return redirect('cart')


def cart_view(request):
    cart_ids = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart_ids)
    total_price = sum(p.price for p in products)
    return render(request, 'pages/cart.html', {
        'title': 'Кошик StalLine',
        'products': products,
        'total_price': total_price,
        'cart_count': len(cart_ids)
    })


def checkout_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        cart_ids = request.session.get('cart', [])
        products = Product.objects.filter(id__in=cart_ids)
        total_price = sum(p.price for p in products)
        products_summary = ", ".join([f"{p.title} ({p.price} грн)" for p in products])

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            phone=phone,
            total_price=total_price,
            products_summary=products_summary
        )

        send_mail(
            subject=f'Нове замовлення №{order.id} - StalLine',
            message=f'Телефон: {phone}\nСума: {total_price} грн\nТовари: {products_summary}',
            from_email='neblivolyn@gmail.com',
            recipient_list=['neblivolyn@gmail.com'],
            fail_silently=False,
        )
        request.session['cart'] = []
        return render(request, 'pages/success.html', {'title': 'Дякуємо за покупку!'})
    return redirect('cart')


# --- Підписка ---
def subscribe_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Subscriber.objects.get_or_create(email=email)
    return redirect(request.META.get('HTTP_REFERER', 'home'))


# --- Авторизація ---
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'pages/register.html', {'form': form, 'title': 'Реєстрація StalLine'})


@login_required
def profile_view(request):
    if request.user.is_staff or request.user.is_superuser:
        orders = Order.objects.all().order_by('-created_at')
        title = "Панель адміністратора"
    else:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        title = "Особистий кабінет"
    return render(request, 'pages/profile.html', {'orders': orders, 'title': title})