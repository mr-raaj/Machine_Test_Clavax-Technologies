from django import forms
from .models import Student

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ActivationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['is_active']
