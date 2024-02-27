from django.contrib import admin
from .models import Hp, Customer_info, Usercomment
from .models import Lenovo
from .models import Asus
from .models import Dell


class HpAdmin(admin.ModelAdmin):
    list_display = (
        "product_image", "product_model", "product_spec1", "product_spec2", "product_spec3", "product_amount")


admin.site.register(Hp, HpAdmin)


class LenovoAdmin(admin.ModelAdmin):
    list_display = (
        "product_image", "product_model", "product_spec1", "product_spec2", "product_spec3", "product_amount")


admin.site.register(Lenovo, LenovoAdmin)


class AsusAdmin(admin.ModelAdmin):
    list_display = (
        "product_image", "product_model", "product_spec1", "product_spec2", "product_spec3", "product_amount")


admin.site.register(Asus, AsusAdmin)


class DellAdmin(admin.ModelAdmin):
    list_display = (
        "product_image", "product_model", "product_spec1", "product_spec2", "product_spec3", "product_amount")


admin.site.register(Dell, DellAdmin)


class Customer_infoAdmin(admin.ModelAdmin):
    list_display = (
        "select_product", "full_name", "email", "mob_no1", "mob_no2", "address")


admin.site.register(Customer_info, Customer_infoAdmin)


class UsercommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "comment")


admin.site.register(Usercomment, UsercommentAdmin)
