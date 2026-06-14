from django.db import models
from django.contrib.auth.models import User  # ОЦЕЙ РЯДОК ОБОВ'ЯЗКОВИЙ ДЛЯ ЗАМОВЛЕНЬ


# Таблиця 1: Категорії
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категорії"


# Таблиця 2: Бренди (Виробники)
class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва бренду")
    country = models.CharField(max_length=100, verbose_name="Країна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Бренди"


# Таблиця 3: Товари
# Таблиця 3: Товари
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва товару")

    # НОВЕ ПОЛЕ ДЛЯ ОПИСУ (можна форматувати через адмінку)
    description = models.TextField(verbose_name="Опис товару", blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name="Бренд")
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Фото товару")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Товари"


# Таблиця 4: Оцінки товарів
class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings', verbose_name="Товар")
    score = models.IntegerField(verbose_name="Оцінка (1-5)")

    class Meta:
        verbose_name_plural = "Оцінки"


# Таблиця 5: Підписники на розсилку
class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")

    class Meta:
        verbose_name_plural = "Підписники"


# Таблиця 6: Замовлення (Лаба 8)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Покупець")
    phone = models.CharField(max_length=20, verbose_name="Номер телефону")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Загальна сума")
    products_summary = models.TextField(verbose_name="Склад замовлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення №{self.id} — {self.phone}"