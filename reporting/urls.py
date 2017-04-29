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
    url(r'^cem$', views.cem_list, name='cem_list'),
    url(r'^newcem$', views.cem_create, name='cem_new'),
    url(r'^editcem/(?P<pk>\d+)$', views.cem_update, name='cem_edit'),
    url(r'^deletecem/(?P<pk>\d+)$', views.cem_delete, name='cem_delete'),
    url(r'^cemreports$', views.cem_reports, name='cem_reports'),
    url(r'^docx_replace_regex/(?P<regex>\d+)/(?P<replace>(\d+))/$', views.docx_replace_regex, name='docx_replace_regex'),




]