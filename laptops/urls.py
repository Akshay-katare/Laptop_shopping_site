from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact,name='contact'),
    path('hpfun', views.hpfun, name='hpfun'),
    path('lenovofun', views.lenovofun, name='lenovofun'),
    path('asusfun', views.asusfun, name='asusfun'),
    path('dellfun', views.dellfun, name='dellfun'),
    path('form', views.form, name='form'),
    path('form1', views.form1, name='form1'),
    path('form2', views.form2, name='form2'),
    path('form3', views.form3, name='form3'),
    # path('get_info', views.get_info, name='get_info'),
    # path('page2/<str:name>/', views.page2, name='page2'),
]
