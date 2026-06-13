from django.db import models


# Таблиця 1: Категорії (наприклад: Столи, Дивани)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    # Обов'язкові поля за завданням: створено та оновлено
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


# Таблиця 3: Товари (Об'єднана з Категоріями та Брендами)
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    # Зв'язок 1-до-багатьох (ForeignKey) з таблицею Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")

    # Зв'язок 1-до-багатьох (ForeignKey) з таблицею Brand
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name="Бренд")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Товари"