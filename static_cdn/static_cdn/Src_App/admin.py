from django.contrib import admin
from .models import Order , Product , Cart_Product , Manufacturer 




class Manufacturer_Admin(admin.ModelAdmin):

    list_display = ['name']


class Product_Admin(admin.ModelAdmin):

    list_display = ['name' , 'manufacturer' ,  'price' ]

class Order_Admin(admin.ModelAdmin):

    list_display = [ 'user' , ]
    readonly_fields = ['user' , 'contact_number' , 'payment_done' ,'payment_method' , 'country' , 'date' , 'total_price' ]
    search_fields = ['user' , 'contact_number' , 'payment_method' , 'country' , 'date' , 'total_price']




admin.site.register(Product , Product_Admin)
admin.site.register(Order  ,Order_Admin)
admin.site.register(Manufacturer , Manufacturer_Admin)