from xmlrpc.client import boolean
from django.db import models
from traitlets import default

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Product(models.Model):
    # Changed from models.AutoField to models.AutoField()
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images', default="")

    def __str__(self):
        return self.product_name
    

class Product2(models.Model):
    # Changed from models.AutoField to models.AutoField()
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images', default="")

    def __str__(self):
        return self.product_name


from django.db import models

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.DecimalField(max_digits=500000, decimal_places=2, default=0.00)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    oid = models.CharField(max_length=50, blank=True)
    amountpaid = models.BooleanField(default=False)  # Updated to BooleanField
    paymentstatus = models.BooleanField(default=False)  # Updated to BooleanField
    phone = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name



class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."