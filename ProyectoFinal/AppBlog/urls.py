from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
]