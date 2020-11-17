from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Post


class HomeView(ListView):
    template_name = 'core/index.html'
    queryset = Post.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)


class PostView(ListView):
    """Posts view"""
    template_name = 'core/index.html'

    def get_queryset(self, **kwargs):
        """Returns active posters posts"""
        return Post.objects.filter(is_active=True,
                                   poster=self.request.user)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)
