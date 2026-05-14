from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa
    path('login/', views.login_view, name='login'),  # Login sayfası
    path('dashboard', views.dashboard_view, name='dashboard'),  # Dashboard sayfası # Dashboard
    path('add_order/', views.add_order, name='add_order'), 
    path('index3/', views.index3, name='index3'),
    path('admin/', admin.site.urls),
]
