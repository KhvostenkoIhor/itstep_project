from django.urls import path

from .views import (
					PostView,
					HomeView,
)


urlpatterns = [
	path('', HomeView.as_view()),
	path('posts/', PostView.as_view()),

]
