from django import forms
from .models import Password
from django.contrib.auth.models import User


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ('nameTag', 'authorName', 'passwordStr', 'description')

        widgets = {
            'authorName': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'authID', 'type' : 'hidden'}),
        #,
            'nameTag': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Some name tag"}),
            'passwordStr': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Your Password"}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "Some description"}),
        }
