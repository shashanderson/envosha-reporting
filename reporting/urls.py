from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cem/$', views.invoice_view, name='invoice_view'),
    url(r'^form/$', views.form_view, name='form_view'),
    url(r'^index/$', views.index_view, name='index_view'),
    url(r'^dashboard/$', views.dashboard_view, name='dashboard_view'),


]