from django.shortcuts import render

from django.http import HttpResponse

def home(request, *args, **kwargs) -> HttpResponse:
	"""Home view"""

	return HttpResponse("Home page")






