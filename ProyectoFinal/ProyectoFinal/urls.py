from django.contrib import admin
from django.urls import path, include
from ProyectoFinal.views import welcome
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', welcome),
    path('', include('AppBlog.urls')),
    path('AppBlog/', include('AppBlog.urls')),
    path('mensajes/', include("mensajes.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
