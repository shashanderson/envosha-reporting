from django import forms
from django.contrib.auth.forms import AuthenticationForm


# If you don't do this you cannot use Bootstrap CSS
from reporting.models import Customer


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class InvoiceForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
        ('html', 'HTML'),
    )
    number = forms.CharField(label='Invoice #')
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    subject = forms.CharField()
    amount = forms.DecimalField()
    format = forms.ChoiceField(choices=FORMAT_CHOICES)
