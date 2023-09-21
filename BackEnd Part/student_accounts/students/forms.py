from django import forms

class StudentActivationForm(forms.Form):
    is_active = forms.BooleanField(required=False)