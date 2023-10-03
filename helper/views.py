from django.shortcuts import render, redirect
from django.views  import View
from .models import Product, Customer, Cart
from django.db.models import Count
from . forms import CustomerForm, CustomerProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
import uuid


# Create your views here.
def home(request):
    return render(request,'helper/index.html')

def about(request):
    return render(request,'helper/about.html')

def contact(request):
    return render(request,'helper/contact.html')

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'helper/address.html',locals())

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for i in cart:
        value = i.quantity * i.product.dprice
        amount += value
    totalamount = amount + 40
    return render(request,'helper/addtocart.html', locals())

def pluscart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for i in cart:
            value = i.quantity * i.product.dprice
            amount += value
        totalamount = amount + 40
        print(prod_id)
        data = {
            'quantity':c.quantity,
            'amount': amount,
            "totalamount" : totalamount
        }
    return JsonResponse(data)

def minuscart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for i in cart:
            value = i.quantity * i.product.dprice
            amount += value
        totalamount = amount + 40
        print(prod_id)
        data = {
            'quantity':c.quantity,
            'amount': amount,
            "totalamount" : totalamount
        }
    return JsonResponse(data)

def removecart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for i in cart:
            value = i.quantity * i.product.dprice
            amount += value
        totalamount = amount + 40
        print(prod_id)
        data = {
            'amount': amount,
            "totalamount" : totalamount
        }
    return JsonResponse(data)


class CategoryView(View):
    def get(self, request, value):
        product = Product.objects.filter(category=value)
        title = product.values('title')
        return render(request,'helper/category.html', locals())

class CategoryTitle(View):
    def get(self, request, value):
        product = Product.objects.filter(title=value)
        title = Product.objects.filter(category = product[0].category ).values('title')
        return render(request,'helper/category.html', locals())
    
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request,'helper/productdetail.html', locals())
    
class RegistrationView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request,'helper/registration.html', locals())
    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulation! Profile save Successful")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request,'helper/registration.html', locals())
    

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request,'helper/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, zipcode=zipcode,
                           state=state)
            reg.save()
            messages.success(request,"Congratulation! User Registration is Successful")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request,'helper/registration.html', locals())
    

class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'helper/updateaddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.state = form.cleaned_data['state']
            add.save()
            messages.success(request,"Congratulation! User Registration is Successful")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('address')

class Checkout(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for i in cart_items:
            value = i.quantity * i.product.dprice
            famount += value
        totalamount = famount + 40
        razoramount = int(totalamount)
        order_id = str(uuid.uuid4())
        return render(request,'helper/checkout.html', locals())