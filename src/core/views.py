from django.shortcuts import render

from django.http import HttpResponse

def home(request, *args, **kwargs) -> HttpResponse:
	"""Home view"""
	#TODO RESUME FROM HERE
	return HttpResponse("<h1>Home page</h1>")

def about(request, *args, **kwargs) -> HttpResponse:
	"""About view"""

	return HttpResponse("About page")




