from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number')

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    def save(self, commit=True, user=None):
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        user.save()



    @staticmethod
    def __check_digit(word: str) -> bool:
        for letter in word:
            if letter.isdigit():
                return True     

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not (self.__check_digit(first_name)):
            raise forms.ValidationError('First name must include at least 1 digit')

        return first_name


    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not (self.__check_digit(last_name)):
            raise forms.ValidationError('Last name must include at least 1 digit')

        return last_name



