from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки админки для категорий"""
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}  # Автозаполнение slug из name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Настройки админки для товаров"""
    list_display = ['name', 'category', 'price', 'stock', 'available']
    list_filter = ['available', 'category', 'created']
    list_editable = ['price', 'stock', 'available']  # Редактирование прямо в списке
    prepopulated_fields = {'slug': ('name',)}

class OrderItemInline(admin.TabularInline):
    """Встроенное отображение товаров заказа"""
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Настройки админки для заказов"""
    list_display = ['id', 'user', 'first_name', 'last_name', 'email',
                   'address', 'postal_code', 'city', 'paid', 'status']
    list_filter = ['paid', 'status', 'created']
    inlines = [OrderItemInline]  # Показываем товары заказа