from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null =True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField(default="null" ,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name

class oldPassWord(models.Model):
    customer = models.ForeignKey(Customer, null =True,blank=True, on_delete=models.CASCADE)
    oldPassWord = models.CharField(max_length=100,null=True,default = "null")
    date = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.customer.name
     

class Discount(models.Model):
    customer = models.OneToOneField(Customer, null =True,blank=True, on_delete=models.CASCADE)
    discount50 = models.CharField(max_length=10,null=True)
    amount50 = models.IntegerField(default=0, null=True, blank=True)
    discount30 = models.CharField(max_length=10,null=True)
    amount30 = models.IntegerField(default=0, null=True, blank=True)
    discount20 = models.CharField(max_length=10,null=True)
    amount20 = models.IntegerField(default=0, null=True, blank=True)
    complete = models.BooleanField(default=False)

class Income(models.Model):
    total_revenue= models.DecimalField(max_digits=8,null=True,decimal_places=2)  
    total_cost = models.DecimalField(max_digits=8,null=True,decimal_places=2) 
     
    data_create = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.data_create.year)+str("-") + str(self.data_create.month)

    def total_profit(self):
        return self.total_revenue-self.total_cost
class Product(models.Model):
    TYPE = (
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Bag', 'Bag'),
        ('Shoes', 'Shoes'),
        ('Watches', 'Watches'),
    )
    TAGS = (
        ('HOODIE','HOODIE'),
        ('SHIRT','SHIRT'),
        ('Fashion', 'Fashion'),
        ('Lifestyle', 'Lifestyle'),
        ('Denim', 'Denim'),
        ('Streetstyle', 'Streetstyle'),
        ('Crafts', 'Crafts'),
    )
    SIZE = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    name     = models.CharField(max_length=200,null=True)
    priceFilter    = models.IntegerField(   null=True)
    price    = models.DecimalField(max_digits=8,null=True,decimal_places=2)
    favorite = models.CharField(max_length=200, default=0,null=True,blank=True)
    type     = models.CharField(max_length=200,null=True,choices=TYPE)
    description =models.CharField(max_length=200,null=True,blank=True)
    date_created =models.DateTimeField(auto_now_add=True,null=True)
    tag      = models.CharField(max_length=200,null=True,choices=TAGS)
    images1  = models.ImageField(default="null",null=True, blank=True)
    images2  = models.ImageField(default="null",null=True, blank=True)
    images3  = models.ImageField(default="null",null=True, blank=True)
    widthS   = models.FloatField(null=True)
    heightS   = models.FloatField(null=True)
    sleeveS   = models.FloatField(null=True)
    shoulderS = models.FloatField(null=True)
    widthM    = models.FloatField(null=True)
    heightM   = models.FloatField(null=True)
    sleeveM   = models.FloatField(null=True)
    shoulderM = models.FloatField(null=True)
    widthL    = models.FloatField(null=True)
    heightL   = models.FloatField(null=True)
    sleeveL   = models.FloatField(null=True)
    shoulderL = models.FloatField(null=True)
    widthXL    = models.FloatField(null=True)
    heightXL   = models.FloatField(null=True)
    sleeveXL   = models.FloatField(null=True)
    shoulderXL = models.FloatField(null=True)
    widthXXL    = models.FloatField(null=True)
    heightXXL   = models.FloatField(null=True)
    sleeveXXL   = models.FloatField(null=True)
    shoulderXXL = models.FloatField(null=True)
    amout = models.IntegerField(default= 100,null=True, blank=True)
    cost = models.DecimalField(default=30.0,max_digits=8,null=True,decimal_places=2)


    def tag1(self):
        return self.TAGS


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.images1.url
        except:
            url = ''
        return url
    
    def imageURL2(self):
        try:
            url = self.images2.url
        except:
            url = ''
        return url

    def imageURL3(self):
        try:
            url = self.images3.url
        except:
            url = ''
        return url

class Bill(models.Model):
    product = models.ForeignKey(Product,null =True,blank=True, on_delete=models.CASCADE)
    amount = models.IntegerField(null =True,blank=True)
    cost = models.DecimalField(default=30.0,max_digits=8,null=True,decimal_places=2)
    date_create = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.date_create.year)+str("-") + str(self.date_create.month)+str("-")+str(self.date_create.day)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    discount = models.DecimalField(default=1.0,decimal_places=2,max_digits=3)
    def __str__(self):
        return str(self.id)                                                         

    def get_total_item(self):
        order = self.orderitem_set.all()
        total = sum ([item.get_total for item in order]) 
        return total 

    def get_total_order(self):
        order = self.orderitem_set.all()
        total = sum ([item.quantity for item in order])
        return total


class Blog(models.Model):
    TAG = (
        ('Streetstlye','Streetstlye'),
        ('Craft','Craft'),
        ('Fashion','Fashion'),
        ('Denim','Denim'),
        ('Lifestyle','Lifestyle'),
    )
    CATEGORIES = (
        ('Fashion','Fashion'),
        ('Beauty','Beauty'),
        ('Streetstlye','Streetstlye'),
        ('Lifestyle','Lifestyle'),
        ('DIY&Craft','DIY&Craft'),
    )
    name = models.CharField(max_length=100, null=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=200,null=True,choices=TAG)
    categories = models.CharField(max_length=200, default="null" , null=True,choices=CATEGORIES)
    images1  = models.ImageField(default="null",null=True, blank=True)
    detail = models.CharField(max_length=1000,null=True)
    detail1 = models.CharField(max_length=10000,null=True)

    def __str__(self):
        return str(self.name)
    @property
    def imageURL(self):
        try:
            url = self.images1.url
        except:
            url = ''
        return url

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,related_name="list",null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    
    @property
    def get_total(self):
        total = self.product.price *self.quantity
        return total*self.order.discount      

    
class Favorite(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)


class FavoriteProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    favorite = models.ForeignKey(Favorite, on_delete=models.SET_NULL, null=True, blank=True)

class DataOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return str(self.id) 
    
    def get_total_item(self):
        order = self.data_set.all()
        total = sum ([item.get_total for item in order])
        return total

class Data(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    dataOrder = models.ForeignKey(DataOrder, on_delete=models.SET_NULL, null=True)
    date_complete = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    size = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id) 

    @property
    def get_total(self):
        total = self.quantity* self.product.price
        return float(total)



class Shiping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Comment(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null = True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=10000,null=True)
    data_create = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(default=1.0,decimal_places=2,max_digits=3)
    def __str__(self):
        return self.customer.name


class LoginAttempts(models.Model):
    customer = models.ForeignKey(Customer, null =True,blank=True, on_delete=models.CASCADE)
    th = models.AutoField(primary_key=True,blank=True)
    start  = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(auto_now_add=True,null=True,blank=True)