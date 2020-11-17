
from django.contrib.auth import get_user_model

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
#from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm, UserSettingsForm

User = get_user_model()

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('login')

class UserSettingsView(UpdateView):
    template_name = 'users/settings.html'
    form_class = UserSettingsForm
    queryset = User.objects.all()
    success_url = reverse_lazy('users:settings')
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        super().get(request, *args, **kwargs)


