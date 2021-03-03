
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("index/", include('core.urls')),
    path('admin/', admin.site.urls),
]
