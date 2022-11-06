from django.contrib import admin
from django.urls import path, include
from ProyectoFinal.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('AppBlog', include('AppBlog.urls'))
]
