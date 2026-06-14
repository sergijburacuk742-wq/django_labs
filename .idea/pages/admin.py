from django.contrib import admin
from .models import Category, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Які колонки показувати в адмінці
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Тут ми виводимо назву, категорію, бренд, ціну та дати
    list_display = ('title', 'category', 'brand', 'price', 'created_at', 'updated_at')
    # Додаємо фільтри збоку для зручності
    list_filter = ('category', 'brand')

    from .models import Order

    @admin.register(Order)
    class OrderAdmin(admin.ModelAdmin):
        list_display = ('id', 'user', 'phone', 'total_price', 'created_at')