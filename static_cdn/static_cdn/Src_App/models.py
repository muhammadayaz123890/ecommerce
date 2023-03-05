from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



class Manufacturer(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):

        return self.name


class Product(models.Model):

    img = models.ImageField(default='' , upload_to='products' , null=False)
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer , default='' ,  on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=60)
    is_most_ordered = models.BooleanField(default=False)
    is_most_popular = models.BooleanField(default=False)
    is_trending = models.BooleanField()
    orders = models.IntegerField(default=0)
    is_in_stock = models.BooleanField(default=True)
    

    def __str__(self):

        return self.name
    



class Cart_Product(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username


    
class Order(models.Model):
    
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    payment_method = models.CharField(max_length=40 , null=True ,choices=(('Paypal', 'Paypal'),('Cash_on_delivery' , 'Cash_on_delivery'),('Stripe', 'Stripe')))
    country = models.CharField(max_length=50, choices=(('Pakistan' , 'Pakistan'),('India' , 'India'),('Bangladesh' , 'Bangladesh')) , null=True)
    payment_done = models.BooleanField(default=False)
    street_address = models.CharField(max_length=100 , null=False, default="")
    contact_number = models.CharField(max_length=50 , null=True )
    date = models.DateTimeField(auto_now_add=True , null=True)
    total_price = models.IntegerField(null=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):

        return self.user.username

