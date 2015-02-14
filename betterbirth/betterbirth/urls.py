from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from betterbirthapp.views import MotherListView, MotherDetailView, do_action
from betterbirthapp.models import Mother

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', lambda x: HttpResponseRedirect('/mothers/list/all')),

  url(r'^accounts/login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
  url(r'^accounts/logout', 'django.contrib.auth.views.logout', {'next_page': '/'}),
  url(r'^mothers/list/(?P<category>\w+)',
 	 MotherListView.as_view(template_name='record_list.html'),
  	name='mothers_list'),
  url(r'^mothers/list/all',
  	MotherListView.as_view(template_name='record_list.html',
  		model=Mother),
  	name='mothers_list_all'),
  url(r'^mothers/manage/(?P<id>\d+)/$',
  	MotherDetailView.as_view(template_name='mother_manage.html', model=Mother, context_object_name='mother'),
  	name='mother_manage'),
  url(r'^action',
  	do_action,
  	name='do_action'),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

