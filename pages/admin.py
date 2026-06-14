from django.contrib import admin
from .models import Category, Brand, Product, ProductImage, Rating, Subscriber, Order

# Налаштування для галереї
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

# Реєструємо товар разом із галереєю
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['title', 'price', 'category', 'brand']

# Реєструємо всі інші таблиці (зверніть увагу: тут НЕМАЄ Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Rating)
admin.site.register(Subscriber)
admin.site.register(Order)