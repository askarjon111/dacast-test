from django.contrib import admin
from django.urls import path
from requests.api import request
from dacast import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.uploadVideo)
]
