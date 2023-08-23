
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registros.urls')),
    path('', include('mi_app.urls')),
]