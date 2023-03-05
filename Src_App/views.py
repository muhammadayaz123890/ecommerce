from django.shortcuts import render
from django.core import serializers
import sys
import requests
from .models import Product
from datetime import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password 
from django.contrib.auth import login , logout 
import random
from django.contrib import messages
from django.shortcuts import redirect
from .models import Cart_Product
from .models import Order
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
import cv2 



def Home(request):

    



    products = None
    context = {}
    r_list = []
    id_list = []
    products = Product.objects.all()

    #### Taking Only Newly added 8 products to show on the first section of the index page #######

    last = len(products)
    first = last - 8
    some = products[first:last]

    products = some[::-1]
    
    context['products'] = products

    ######### FOR RANDOM PRODUCTS ##########################################################

    for product in products:
        id = int(product.id)
        id_list.append(id)


    max_id = max(id_list)
    min_id = min(id_list)


    r_1 = random.randint(min_id , max_id)
    r_2 = random.randint(min_id , max_id)
    r_3 = random.randint(min_id , max_id)
    r_4 = random.randint(min_id , max_id)
    r_5 = random.randint(min_id , max_id)
    r_6 = random.randint(min_id , max_id)
    r_7 = random.randint(min_id , max_id)
    r_8 = random.randint(min_id , max_id)
    
    s_list = []

    s_list.append(r_1)
    s_list.append(r_2)
    s_list.append(r_3)
    s_list.append(r_4)
    s_list.append(r_5)
    s_list.append(r_6)
    s_list.append(r_7)
    s_list.append(r_8)
    
    for i in s_list:
        product_ = Product.objects.get(id=i)
        r_list.append(product_)

    context['r_products'] = r_list


    ####### FOR MAXIMUM ORDERED PRODUCTS INSHALLAH ##############################################


    o_list = []
    u_list = []
    some_list = []

    for product in products:
        o = int(product.orders)
        o_list.append(o)
    
    o_1 = max(o_list)
    u_list.append(o_1)
    o_list.remove(o_1)
    o_2 = max(o_list)
    u_list.append(o_2)
    o_list.remove(o_2)
    o_3 = max(o_list)
    u_list.append(o_3)
    o_list.remove(o_3)
    o_4 = max(o_list)
    u_list.append(o_4)
    o_list.remove(o_4)
    o_5 = max(o_list)
    u_list.append(o_5)
    o_list.remove(o_5)
    o_6 = max(o_list)
    u_list.append(o_6)
    o_list.remove(o_6)
    o_7 = max(o_list)
    u_list.append(o_7)
    o_list.remove(o_7)
    o_8 = max(o_list)
    u_list.append(o_8)
    o_list.remove(o_8)
    
    
    for u in u_list:
        o_p = Product.objects.get(orders=u)
        some_list.append(o_p)
    
    context['o_products'] = some_list

    ######################################################################################################

    return render(request , 'index.html' , context )



def Add_to_cart(request):
    check_product = None
    try:

        if request.method == 'GET':
            id = request.GET.get("product_id")
            if id:
                id = int(id)

                product = Product.objects.get(pk=id)

                user = request.user
                try:
                    check_product = Cart_Product.objects.get(user=user,product=product)
                except Exception as e:
                    print(e)
                if check_product:
                    print("Already there")
                elif not check_product:
                    new_cart_product = Cart_Product.objects.create(user=user,product=product)
                    new_cart_product.save()
                else:
                    print("Product Unavailable")

    except Exception as e:
        print(e)
        
    return JsonResponse({"Done" : "Product has been added"})




def Login(request):

    users = User.objects.all()

    if request.method == 'POST':

        email = request.POST.get("email")
        password = request.POST.get("password")

        password = str(password)

        if email != None and password != None:
            
            for user in users:
                if user.email == email:
                    if user.check_password(password):
                        print("User Exists")
        
                    login(request , user)
                    return redirect("home")
                else:
                    messages.warning(request , "Bad Credentails")

    return render(request , 'sign_in.html')



def Register(request):
    users = User.objects.all()

    if request.method == 'POST':

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        email = str(email)

        username = email.split("@")[0]

        print(username)

        for user in users:

            if user.email == email:
                print("Email already exits")
                messages.warning(request , "Email Already Exists")
            else:
                new_user = User.objects.create(
                    username=username,
                    email=email,
                    password=password
                )
                
                login(request , new_user)

                new_user.save()

    return render(request , 'register.html')


def Profile(request):   



    return render(request , 'profile.html')


def All(request):

    context = {}

    #####################################
    products = Product.objects.all()

    context['products'] = products

    return render(request , 'general_products.html' , context)



def Search(request):

    context = {}

    if request.method == "GET":
        
        key = request.GET.get("search_key") 

        context['your_key'] = key

        products = Product.objects.filter(name__icontains=key)

        if products:
            context['products'] = products
        else:
            products = Product.objects.filter(description__icontains=key)
            context['products'] = products
    return render(request, 'search_result_products.html' , context)



def Specific_Product(request):
    context = {}
    user = request.user

    ############################################################
    
    if request.method == 'POST':

        number = request.POST.get("number")
        amount = request.POST.get("amount")
        address = request.POST.get("address")
        product_id = request.POST.get("product_id")
        country = request.POST.get("country_name")
        payment_method = request.POST.get('payment_method')


        country = str(country).capitalize()
        

        if product_id != None:
            product_id = int(product_id)
            product = Product.objects.get(pk=product_id)
            context['product'] = product

    all_orders = Order.objects.all()


    new_order = Order.objects.create(
        user=request.user
    )

    new_order.product.add(product)
    new_order.payment_done = False
    new_order.payment_method = payment_method
    new_order.country = country
    new_order.total_price = product.price
    new_order.save()

    return render(request , 'buy_product.html' , context)


def Place_Order(request):

    context = {}

    if request.method == 'GET':

        id = request.GET.get('product_id')

        if id is not None:
            id = int(id)

            product = Product.objects.get(pk=id)

            context['product'] = product

            
    return render(request , 'placing_order.html' , context)


def Place_Cart_Order(request):
    pro_ids = []
    cart_products = Cart_Product.objects.filter(user=request.user)

    if request.method == 'POST':
        con_number = request.POST.get("number")
        country = request.POST.get("country_name")
        address = request.POST.get("address")
        payment_method = request.POST.get("payment_method")
    
    for product in cart_products:
        id = int(product.product.id)
        pro_ids.append(id)
    
    new_order = Order.objects.create(user=request.user)

    for id in pro_ids:
        product = Product.objects.get(pk=id)
        new_order.product.add(product)
    
    new_order.contact_number = con_number
    new_order.payment_done = False
    new_order.country = country
    new_order.payment_method = payment_method 
    
    total = (request.session['total'])
    
    if total:
        total = int(total)
    
    new_order.total_price = total
    new_order.completed = False
    new_order.save()
    
    if new_order.payment_method == 'Stripe':

        return redirect("stripe_cart")
    if new_order.payment_method == 'Paypal':

        return redirect("paypal_cart")
    
    if new_order.payment_method == 'Cash_on_delivery':

        return JsonResponse({"mess" : "Order Placed"})

    
    return render(request , 'buy_cart_products.html')


@login_required(login_url='login')
def Paypal_cart(request):


    return render(request , 'paypal_cart_page.html')


@login_required(login_url='login')
def _Cart(request):
    context = {}
    id_list = []
    user = request.user
    total = 0
    product_list = []
    cart_products = Cart_Product.objects.filter(user=user)

    products = Cart_Product.objects.filter(user=user).values()

    for i in products:
        for key in i:
            if key == 'product_id':
                id_list.append(i[key])
    
    product = None

    for id in id_list:
        id = int(id)
        product = Product.objects.get(pk=id).price
        product_list.append(product)
    
    for price in product_list:
        total += price

    context['total'] = total

    context['cart_products'] = cart_products

    request.session['total'] = total


    return render(request , 'cart.html' , context)


@login_required(login_url='login')
def Stripe_cart_page(request):

    return render(request , 'stripe_cart.html')


def Logout(request):

    logout(request)
    return redirect("home")


def Remove_Product(request):

    if request.method == 'GET':
        id = request.GET.get("product_id")
        if id:
            id = int(id)
            product = Cart_Product.objects.get(pk=id)

            if product:
                product.delete()
                print("Removed")

    return JsonResponse({"done": "Product has been removed"})


def Cart_Checkout(request):

    context = {}
    user = request.user

    cart_products = Cart_Product.objects.filter(user=user)

    print(cart_products)

    context['cart_products'] = cart_products

    return render(request , 'checkout_cart.html' , context)

