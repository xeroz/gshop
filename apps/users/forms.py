from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class Registrationform(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super(Registrationform, self).save(commit=False)
        user.first_name = cleaned_data['first_name']
        user.last_name = cleaned_data['last_name']
        user.email = cleaned_data['email']

        if commit:
            user.save()

        return user

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#     fields = ('description', 'city', 'website', 'phone')
