from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cem/$', views.invoice_view, name='invoice_view'),
    url(r'^pd/$', views.write_pdf_view, name='write_pdf_view'),
    url(r'^pdo/$', views.html_to_pdf_view, name='html_to_pdf_view'),


]