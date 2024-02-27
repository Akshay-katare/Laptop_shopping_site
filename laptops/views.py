

from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import loader
from .models import Hp, Lenovo, Asus, Dell, Customer_info, Usercomment


def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        arpan = Usercomment(name=name, email=email, phone=phone, comment=comment)
        arpan.save()

    return render(request, 'contact.html')


def hpfun(request):
    product_details = Hp.objects.all().values()
    template = loader.get_template('hp_products.html')
    context = {
        'product_details': product_details,
    }
    return HttpResponse(template.render(context, request))


def lenovofun(request):
    product_details = Lenovo.objects.all().values()
    template = loader.get_template('lenovo_products.html')
    context = {
        'product_details': product_details,
    }
    return HttpResponse(template.render(context, request))


def asusfun(request):
    product_details = Asus.objects.all().values()
    template = loader.get_template('asus_products.html')
    context = {
        'product_details': product_details,
    }
    return HttpResponse(template.render(context, request))


def dellfun(request):
    product_details = Dell.objects.all().values()
    template = loader.get_template('dell_products.html')
    context = {
        'product_details': product_details,
    }
    return HttpResponse(template.render(context, request))


# def form(request):
#     product_details = Hp.objects.all().values()
#     template = loader.get_template('Order_details.html')
#     context = {
#         'product_details': product_details,
#     }
#     return HttpResponse(template.render(context, request))


def form(request):
    product_details = Hp.objects.all().values()
    template = loader.get_template('Order_details.html')
    context = {
        'product_details': product_details,
    }

    if request.method == "POST":
        select_product = request.POST.get('select_product')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mob_no1 = request.POST.get('mob_no1')
        mob_no2 = request.POST.get('mob_no2')
        address = request.POST.get('address')
        doubts = Customer_info(select_product=select_product, full_name=full_name, email=email, mob_no1=mob_no1,
                               mob_no2=mob_no2, address=address)
        doubts.save()

    return HttpResponse(template.render(context, request))


def form1(request):
    product_details = Lenovo.objects.all().values()
    template = loader.get_template('order_for_lenovo.html')
    context = {
        'product_details': product_details,
    }
    if request.method == "POST":
        select_product = request.POST.get('select_product')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mob_no1 = request.POST.get('mob_no1')
        mob_no2 = request.POST.get('mob_no2')
        address = request.POST.get('address')
        doubts = Customer_info(select_product=select_product, full_name=full_name, email=email, mob_no1=mob_no1,
                               mob_no2=mob_no2, address=address)
        doubts.save()

    return HttpResponse(template.render(context, request))


def form2(request):
    product_details = Asus.objects.all().values()
    template = loader.get_template('orders_for_asus.html')
    context = {
        'product_details': product_details,
    }

    if request.method == "POST":
        select_product = request.POST.get('select_product')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mob_no1 = request.POST.get('mob_no1')
        mob_no2 = request.POST.get('mob_no2')
        address = request.POST.get('address')
        doubts = Customer_info(select_product=select_product, full_name=full_name, email=email, mob_no1=mob_no1,
                               mob_no2=mob_no2, address=address)
        doubts.save()

    return HttpResponse(template.render(context, request))


def form3(request):
    product_details = Dell.objects.all().values()
    template = loader.get_template('orders_for_dell.html')
    context = {
        'product_details': product_details,
    }

    if request.method == "POST":
        select_product = request.POST.get('select_product')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mob_no1 = request.POST.get('mob_no1')
        mob_no2 = request.POST.get('mob_no2')
        address = request.POST.get('address')
        doubts = Customer_info(select_product=select_product, full_name=full_name, email=email, mob_no1=mob_no1,
                               mob_no2=mob_no2, address=address)
        doubts.save()

    return HttpResponse(template.render(context, request))

# Create your views here.
