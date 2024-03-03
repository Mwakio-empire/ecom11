from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #A USER CAN ONLY HAVE ONE CUSTOMER AND A CUSTOMER CAN ONLY HAVE ONE USER
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

#DIGITAL IS A BOOLEAN VALUE IF TRUE, WE DON'T NEED TO SHIP IT ELSE IT IS A PHYSICAL PRODUCT THAT NEEDS TO BE SHIPPED
class Product(models.Model):
    name = models.CharField(max_length=200, )
    price = models.FloatField()
    digital = models.BooleanField(default=False)#meaning by default each item is a physical item
    image = models.ImageField( null=True, blank=True)



    def __str__(self):
        return self.name



# RELATIONSHIPS
# COMPLETE DEFAULT FALSE = one can continue adding goods to cart when it is not shipped
#ondelete if a customer is deleted this ensures that their order is not deleted from the cart upon refreshing therefore ondelete=models.SET_NULL
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)#changes the date value to match when shipping is done... i think
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True, unique=True)

    def __str__(self):
        return self.transaction_id

#CHILD TABLE
#A SINGLE ORDER CAN HAVE MULTIPLE ITEMS
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
      customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
      order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
      shipping_address = models.CharField(max_length=200, null=True, )
      city = models.CharField(max_length= 200, null=True)

      def __str__(self):
          return self.shipping_address


