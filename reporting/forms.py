from django import forms
from django.contrib.auth.forms import AuthenticationForm

from reporting.models import AreaPersonalType, Parameter


# If you don't do this you cannot use Bootstrap CSS


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class BookForm(forms.ModelForm):
    class Meta:
        model = AreaPersonalType
        fields = ('company', 'point', 'work_unit', 'method', 'flow_rate', 'media',
                  'technique', 'area_personal_type', 'classification_type', 'classification_value')


class ParameterForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = (  'area_personal_type', 'parameter_value')
