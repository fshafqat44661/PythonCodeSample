from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import CharField

STATE_CHOICES = (
    ('Karachi', 'Karachi'),
    ('Lahore', 'Lahore'),
    ('Faisalabad','Faisalabad'),
    ('Rawalpindi', 'Rawalpindi'),
    ('Gujranwala', 'Gujranwala'),
    ('Peshawar', 'Peshawar'),
    ('Multan', 'Multan'),
    ('Islamabad', 'Islamabad'),
    ('Gujrat','Gujrat'),
    ('Okara', 'Okara')
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    # ('M', 'Mobile'),
    # ('L', 'Laptop'),
    # ('TW', 'Top Wear'),
    # ('BW', 'Bottom Wear')
    ('Healthy_Food', 'Healthy Food'),
    ('Gym_Box', 'Gym box'),
    ('TAF', 'Traditional Asian Food'),
    ('CakesADD', 'Cake and Dessert dishes'),
    ('OGP', 'Office Gatherings and Parties'),
    ('Breakfast', 'Breakfast'),
    ('Vegan', 'Vegan')

)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.IntegerField()
    discounted_price = models.IntegerField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    product_image = models.ImageField(upload_to = 'productimg')

    def __str__(self):
        return str(self.id)    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='Pending', max_length=50)
    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


