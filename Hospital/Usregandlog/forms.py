from django import forms
from django.forms import ModelForm, widgets
from .models import Register

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields  = ['name', 'Father_name','DOB', 'sex', 'phone_num']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Father_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'DOB' : forms.DateInput(attrs={'class' : 'form-control'}),
            'sex' : forms.Select(attrs={'class' : 'form-control'}),
            'phone_num' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }
        