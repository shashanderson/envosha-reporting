from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^form/$', views.form_view, name='form_view'),
    url(r'^index/$', views.index_view, name='index_view'),
    url(r'^dashboard/$', views.dashboard_view, name='dashboard_view'),
    url(r'^company$', views.company_list, name='company_list'),
    url(r'^new$', views.company_create, name='company_new'),
    url(r'^edit/(?P<pk>\d+)$', views.company_update, name='company_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.company_delete, name='company_delete'),


]