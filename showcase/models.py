from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False, verbose_name='Nome')
    description = models.TextField(max_length=255, blank=True, verbose_name='Descrição')
    image = models.ImageField(upload_to='products_images/', blank=False, verbose_name='Imagem')
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')
    promotion = models.BooleanField(default=False, verbose_name='Promoção')
    discontinued = models.BooleanField(default=False, verbose_name='Descontinuado')
    registered_in = models.DateTimeField(auto_now=True, verbose_name='Registrado em')

    class Meta:
        db_table = 'products'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(null=False, blank=False, verbose_name='E-mail')
    signed_in = models.DateTimeField(auto_now=True, verbose_name='Assinado em')

    class Meta:
        db_table = 'newsletter'
        verbose_name = 'Boletim Informativo'
        verbose_name_plural = 'Boletins Informativos'

    def __str__(self):
        return self.email
