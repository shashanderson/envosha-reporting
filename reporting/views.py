import re

from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from docx import Document

from reporting.models import Company, AreaPersonalType


@login_required(login_url="login/")
def home(request):
    return render(request, "index.html")


@login_required(login_url="login/")
def form_view(request):
    return render(request, "form.html")


@login_required(login_url="login/")
def index_view(request):
    return render(request, "index.html")


@login_required(login_url="login/")
def dashboard_view(request):
    return render(request, "dashboard.html")


class AreaPersonalTypeForm(ModelForm):
    class Meta:
        model = AreaPersonalType
        fields = ['company', 'point', 'work_unit', 'method', 'flow_rate', 'media', 'technique',
                  'area_personal_type', 'classification_type', 'classification_value']


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_address',
                  'company_country', 'company_contact_no'
            , 'company_pic', 'consultant']


def company_list(request, template_name='company/company_list.html'):
    companys = Company.objects.all()
    data = {}
    data['object_list'] = companys
    return render(request, template_name, data)


# def company_create(request, template_name='company/company_form.html'):
#     form = CompanyForm(request.POST)
#     form2 = AreaPersonalTypeForm(request.POST)
#     if all([form.is_valid(), form2.is_valid()]):
#         form.save()
#         form2.save()
#         return redirect('company_list')
#     else:
#         form = CompanyForm(request.POST)
#         form2 = AreaPersonalTypeForm(request.POST)
#     return render(request, template_name, {'form': form, 'form2': form2})

def company_create(request, template_name='company/company_form.html'):
    form = CompanyForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('company_list')
    else:
        form = CompanyForm(request.POST or None)
    return render(request, template_name, {'form': form})


def company_update(request, pk, template_name='company/company_form.html'):
    company = get_object_or_404(Company, pk=pk)
    # cem = get_object_or_404(AreaPersonalType, pk=id)
    form = CompanyForm(request.POST or None, instance=company)
    cem_form = AreaPersonalTypeForm(request.POST)

    if all([form.is_valid(), cem_form.is_valid()]):
        form.save()
        cem_form.save()
        return redirect('company_list')
    return render(request, template_name, {'form': form, 'cem_form': cem_form})


def company_delete(request, pk, template_name='company/company_confirm_delete.html'):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, template_name, {'object': company})


# new code ############################################################################################


def cem_list(request, template_name='company/cem_list.html'):
    cems = AreaPersonalType.objects.all()
    data = {}
    data['object_list'] = cems
    return render(request, template_name, data)


def cem_create(request, template_name='company/cem_form.html'):
    form = AreaPersonalTypeForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('cem_list')
    else:
        form = AreaPersonalTypeForm(request.POST or None)
    return render(request, template_name, {'form': form})


def cem_update(request, pk, template_name='company/cem_form.html'):
    cem = get_object_or_404(AreaPersonalType, pk=pk)
    form = AreaPersonalTypeForm(request.POST or None, instance=cem)

    if form.is_valid():
        form.save()
        return redirect('cem_list')
    return render(request, template_name, {'form': form})


def cem_delete(request, pk, template_name='company/cem_confirm_delete.html'):
    cem = get_object_or_404(AreaPersonalType, pk=pk)
    if request.method == 'POST':
        cem.delete()
        return redirect('cem_list')
    return render(request, template_name, {'object': cem})


def docx_replace_regex(doc_obj, regex, replace):

    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_replace_regex(cell, regex, replace)


def initiate_replace(param1,param2):
    filename = "ENVOSHA/templates/CEM_Report.docx"
    doc = Document(filename)
    docx_replace_regex(doc, param1, param2)
    doc.save('ENVOSHA/static/CEM_Report_new.docx')


# regex1 = re.compile(r"Baseline")
# replace1 = r"{{ company_name }}"
# regex2 = re.compile(r"{{ naaaaaam }}")
# replace2 = r"{{ xna }} "
# filename = "ENVOSHA/templates/CEM_Report.docx"
# doc = Document(filename)
#
# docx_replace_regex(doc, regex1, replace1)
# docx_replace_regex(doc, regex1, replace1)
# docx_replace_regex(doc, regex2, replace2)
# doc.save('ENVOSHA/static/CEM_Report_new.docx')



def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def custom_404(request):
    return render(request, '404.html', {}, status=404)


def cem_reports(request, template_name='company/cem_reports.html'):
    companys = Company.objects.all()
    data = {}
    data['object_list'] = companys
    return render(request, template_name, data)


