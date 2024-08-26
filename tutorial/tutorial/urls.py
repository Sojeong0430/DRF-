from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from quickstart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',include('quickstart.urls')),
    path('accounts/',include('accounts.urls')),
]
