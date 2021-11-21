# Generated by Django 3.2.9 on 2021-11-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='signed_in',
            field=models.DateTimeField(auto_now=True, verbose_name='Assinado em'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, max_length=255, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='products',
            name='discontinued',
            field=models.BooleanField(default=False, verbose_name='Descontinuado'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products_images/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='products',
            name='promotion',
            field=models.BooleanField(default=False, verbose_name='Promoção'),
        ),
        migrations.AlterField(
            model_name='products',
            name='registered_in',
            field=models.DateTimeField(auto_now=True, verbose_name='Registrado em'),
        ),
        migrations.AlterField(
            model_name='products',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor'),
        ),
        migrations.AlterModelTable(
            name='newsletter',
            table='newsletter',
        ),
        migrations.AlterModelTable(
            name='products',
            table='products',
        ),
    ]
