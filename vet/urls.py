"""
URL configuration for veterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('cliente/',views.cliente, name='cliente'),
    path('veterinario/',views.veterinario, name='veterinario'),
    path('administrador/',views.administrador, name='administrador'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('menu/', views.menu, name='menu'),
    
    path('personas/', views.mostrar_personas, name='mostrar_personas'),
    path('eliminar_persona/', views.eliminar_persona, name='eliminar_persona'),
    path('agregar_persona/', views.agregar_persona, name='agregar_persona'),

    path('mascotas/', views.mostrar_mascotas, name='mostrar_mascotas'),
    path('eliminar_mascota/', views.eliminar_mascota, name='eliminar_mascota'),
    path('agregar_mascota/', views.agregar_mascota, name='agregar_mascota'),

    path('medicamentos/', views.mostrar_medicamentos, name='mostrar_medicamentos'),
    path('eliminar_medicamento/', views.eliminar_medicamento, name='eliminar_medicamento'),
    path('agregar_medicamento/', views.agregar_medicamento, name='agregar_medicamento'),

    path('ordenes/', views.mostrar_ordenes, name='mostrar_ordenes'),
    path('eliminar_orden/', views.eliminar_orden, name='eliminar_orden'),
    path('agregar_orden/', views.agregar_orden, name='agregar_orden'),

    path('hc/', views.mostrar_hc, name='mostrar_hc'),
    path('eliminar_hc/', views.eliminar_hc, name='eliminar_hc'),
    path('agregar_hc/', views.agregar_hc, name='agregar_hc'),

    path('medfact/', views.mostrar_medfact, name='mostrar_medfact'),
    path('eliminar_medfact/', views.eliminar_medfact, name='eliminar_medfact'),
    path('agregar_medfact/', views.agregar_medfact, name='agregar_medfact'),

    path('facturas/', views.mostrar_facturas, name='mostrar_facturas'),
    path('eliminar_factura/', views.eliminar_factura, name='eliminar_factura'),
    path('agregar_factura/', views.agregar_factura, name='agregar_factura'),

]
