from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlaced

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dprice', 'category', 'prodapp']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'state', 'zipcode']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','amount','razorpay_order_id','razorpay_payment_status' ,'razorpay_payment_id','paid'] 

@admin.register(OrderPlaced)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','payment','quantity','ordered_date','status']

