from django.contrib.auth.decorators import login_required
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
from django.shortcuts import render
from templated_docs import fill_template
from templated_docs.http import FileResponse

from reporting.forms import InvoiceForm


@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def invoice_view(request):
    form = InvoiceForm(request.POST or None)

    if form.is_valid():
        doctype = form.cleaned_data['format']
        filename = fill_template(
            'invoice.odt', form.cleaned_data,
            output_format=doctype)
        visible_filename = 'invoice.{}'.format(doctype)

        return FileResponse(filename, visible_filename)
    else:
        return render(request, 'map.html', {'form': form})

