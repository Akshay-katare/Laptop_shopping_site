# Generated by Django 5.0.2 on 2024-02-22 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0006_delete_customerinfo_alter_customer_info_mob_no1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usercomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
