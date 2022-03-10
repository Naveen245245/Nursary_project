from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Owner(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    dp = models.ImageField(upload_to='dp/', default='default.png', blank=True)

    def __str__(self):
        return self.name


class Nursary(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    visiting_card = models.ImageField(
        upload_to='visting_card/', default='default.png', blank=True)
    nursary_photo = models.ImageField(
        upload_to='nursary_photo/', default='default.png', blank=True)
    rows = models.IntegerField()
    columns = models.IntegerField()

    def __str__(self):
        return self.name
    


class Product(models.Model):
    type_choices = (("Tamota", "T"),
                    ("Mirchi", "M"),
                    ("Vanyakaya", "V"),
                    ("Chendu Malli", "CM"),
                    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=type_choices)
    quatity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Farmer(models.Model):
    name = models.CharField(max_length=50)
    adhar_num = models.IntegerField()
    phone_num = models.IntegerField()
    land_survey_num = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Bed(models.Model):
    type_choices = (("E", "Empty"),
                    ("A", "Available"),
                    ("B", "Booked"),
                    ("C", "Completed"),
                    )
    capacity = models.IntegerField(default=10000)
    # created = models.DateField( auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=50, choices=type_choices, default="E")
    nursary = models.ForeignKey('Nursary', on_delete=models.CASCADE)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True,)
    farmer_c = models.ForeignKey(Farmer, on_delete=models.SET_NULL, blank=True, null=True,)
    nursary_p = models.ForeignKey(Nursary, on_delete=models.SET_NULL, blank=True, null=True,)
    qty = models.PositiveIntegerField()
    amount = models.FloatField(blank=True)
    bed = models.ForeignKey(
        Bed, on_delete=models.SET_NULL, blank=True, null=True,)

    def save(self, *args, **kwargs):
        self.amount = self.product.price * self.qty
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.product)+" was purchased By "+str(self.farmer_c)+" from "+str(self.nursary_p)


