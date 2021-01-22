from django import forms
from .models import Password
from django.contrib.auth.models import User


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ('Name_Tag', 'authorName', 'Password_String', 'Description')

        widgets = {
            'authorName': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'authID', 'type' : 'hidden'}),
        #,
            'Name_Tag': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Some name tag"}),
            'Password_String': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Your Password"}),
            'Description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "Some description"}),
        }
