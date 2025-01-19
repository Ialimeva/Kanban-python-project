from django.contrib import admin
from django.urls import path
from home.views import home_view, add_view, addrecord_view

urlpatterns = [
    path('', home_view, name = 'home'),
    path('add/', add_view, name = 'add'),
    path('add/addrecord', addrecord_view, name = 'addrecord'),
    path('admin/', admin.site.urls, name = 'admin'),
]
