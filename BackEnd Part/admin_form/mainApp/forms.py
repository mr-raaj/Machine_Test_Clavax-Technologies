#forms.py

from django import forms
from .models import ClassDetail

class ClassDetailForm(forms.ModelForm):
    class Meta:
        model = ClassDetail
        fields = ['class_name']  # Add more fields as needed
