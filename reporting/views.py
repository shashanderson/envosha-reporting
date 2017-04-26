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


from django.http import HttpResponseNotFound


def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'mypdf.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')


from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def write_pdf_view(request):
    doc = SimpleDocTemplate("/tmp/somefilename.pdf")
    styles = getSampleStyleSheet()
    Story = [Spacer(1, 2 * inch)]
    style = styles["Normal"]
    for i in range(100):
        bogustext = ("This is Paragraph number %s.  " % i) * 20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1, 0.2 * inch))
    doc.build(Story)

    fs = FileSystemStorage("/tmp")
    with fs.open("somefilename.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        return response

    return response


from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


def html_to_pdf_view(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('core/pdf_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response
