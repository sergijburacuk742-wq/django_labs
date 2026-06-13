from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Головна',
        'heading': 'Вітаємо на Головній сторінці!',
        'content': 'Це текст головної сторінки. Звідси можна перейти на інші розділи.',
        'is_home': True  # Вмикає посилання на інші сторінки
    }
    return render(request, 'pages/page.html', context)

def about_view(request):
    context = {
        'title': 'Про нас',
        'heading': 'Про наш проєкт',
        'content': 'Цю сторінку згенеровано за допомогою того самого шаблону, але текст інший!',
        'is_home': False # Вмикає кнопку "Назад"
    }
    return render(request, 'pages/page.html', context)

def contacts_view(request):
    context = {
        'title': 'Контакти',
        'heading': 'Наші контакти',
        'content': 'Зв\'яжіться з нами за телефоном: +38000000000',
        'is_home': False # Вмикає кнопку "Назад"
    }
    return render(request, 'pages/page.html', context)