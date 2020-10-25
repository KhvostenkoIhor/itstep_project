from django.urls import path

from .views import home as home_view
from .views import about as about_view

urlpatterns = [
	path('home/', home_view),
	path('about/', about_view),

]
