from django.contrib.auth.decorators import login_required
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from reporting.models import Company


@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


@login_required(login_url="login/")
def form_view(request):
    return render(request, "form.html")


@login_required(login_url="login/")
def index_view(request):
    return render(request, "index.html")


@login_required(login_url="login/")
def dashboard_view(request):
    return render(request, "dashboard.html")


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_address', 'company_country']


def company_list(request, template_name='company/company_list.html'):
    companys = Company.objects.all()
    data = {}
    data['object_list'] = companys
    return render(request, template_name, data)


def company_create(request, template_name='company/company_form.html'):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('company_list')
    return render(request, template_name, {'form': form})


def company_update(request, pk, template_name='company/company_form.html'):
    company = get_object_or_404(Company, pk=pk)
    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        form.save()
        return redirect('company_list')
    return render(request, template_name, {'form': form})


def company_delete(request, pk, template_name='company/company_confirm_delete.html'):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, template_name, {'object': company})
