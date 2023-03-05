from django.urls import path
from . import views



urlpatterns = [
    path("" , views.Home , name='home'),
    path("login/", views.Login , name='login'),
    path("register_account/" , views.Register , name='register'),
    path("profile/" ,views.Profile , name='profile'),
    path("all_products/" , views.All , name='all_products'),
    path('search/' , views.Search , name='search'),
    path("buy_product/" , views.Specific_Product , name='product'),
    path("place_order/" , views.Place_Order , name='place_order'),
    path("your_cart/" , views._Cart , name='cart'),
    path("logout/" , views.Logout , name='logout'),
    path('add_cart/' , views.Add_to_cart , name='add_to_cart'),
    path("remove_product/" , views.Remove_Product , name='remove_item'),
    path("cart_checkout/" , views.Cart_Checkout , name='cart_checkout'),
    path("cart_order/" , views.Place_Cart_Order , name='cart_order'),
    path("stripe_cart_checkout/" , views.Stripe_cart_page , name='stripe_cart'),
    path("paypal_cart_payment/" , views.Paypal_cart, name='paypal_cart'),
]
