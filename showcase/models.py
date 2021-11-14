from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='products_images/', blank=False)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    promotion = models.BooleanField(default=False)
    discontinued = models.BooleanField(default=False)
    registered_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(null=False, blank=False)
    signed_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
