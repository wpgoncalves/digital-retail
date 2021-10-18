from django.db import models


# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(null=False, blank=False)
    signed_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
