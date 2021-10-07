from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('supplier_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('buyer_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('season_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
        


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=250,null=False, unique=True) 
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('product_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('order_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=False, unique=True)

    def __str__(self):
        return self.courier_name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('delivery_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)