from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Local
    # path('home/', core_views.home),
    path("core/", include("core.urls")),
]
































