from django.db import models


class Hp(models.Model):
    product_image = models.ImageField(upload_to='C:/Users/Asus/PycharmProjects/pythonProject37/static/Hp_images/')
    product_model = models.CharField(max_length=90)
    product_spec1 = models.CharField(max_length=100)
    product_spec2 = models.CharField(max_length=100)
    product_spec3 = models.CharField(max_length=100)
    product_amount = models.IntegerField()


class Lenovo(models.Model):
    product_image = models.ImageField(upload_to='C:/Users/Asus/PycharmProjects/pythonProject37/static/Lenovo_images')
    product_model = models.CharField(max_length=90)
    product_spec1 = models.CharField(max_length=100)
    product_spec2 = models.CharField(max_length=100)
    product_spec3 = models.CharField(max_length=100)
    product_amount = models.IntegerField()


class Asus(models.Model):
    product_image = models.ImageField(upload_to='C:/Users/Asus/PycharmProjects/pythonProject37/static/Asus_images/')
    product_model = models.CharField(max_length=90)
    product_spec1 = models.CharField(max_length=100)
    product_spec2 = models.CharField(max_length=100)
    product_spec3 = models.CharField(max_length=100)
    product_amount = models.IntegerField()


class Dell(models.Model):
    product_image = models.ImageField(upload_to='C:/Users/Asus/PycharmProjects/pythonProject37/static/Dell_images/')
    product_model = models.CharField(max_length=90)
    product_spec1 = models.CharField(max_length=100)
    product_spec2 = models.CharField(max_length=100)
    product_spec3 = models.CharField(max_length=100)
    product_amount = models.IntegerField()


class Customer_info(models.Model):
    select_product = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    mob_no1 = models.IntegerField()
    mob_no2 = models.IntegerField()
    address = models.TextField()


class Usercomment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    comment = models.TextField()
