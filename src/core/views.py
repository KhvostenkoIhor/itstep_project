from django.views.generic import ListView, CreateView, View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Post
from .forms import PostCreationForm


class HomeView(ListView):
    template_name = 'core/index.html'
    #queryset = Post.objects.exclude(is_active=False, poster=self.request.user)

    def get_queryset(self, **kwargs):
        return Post.objects.exclude(is_active=False, poster=self.request.user)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)


class PostsView(ListView):
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

class PostCreateView(CreateView):
    '''Provides post creation by form'''
    template_name = 'core/post_creation.html'
    form_class = PostCreationForm
    model = Post

    def post(self, request, *args, **kwargs):
        form = PostCreationForm(data=request.POST)
        form.save(user=request.user)

        return redirect('core:my_posts')
           
    
    
    

