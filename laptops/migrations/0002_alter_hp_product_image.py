# Generated by Django 5.0.2 on 2024-02-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hp',
            name='product_image',
            field=models.ImageField(upload_to='C:/Users/Asus/PycharmProjects/pythonProject37/static/'),
        ),
    ]
