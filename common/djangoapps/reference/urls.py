from django.conf.urls import patterns, url

from reference import views

'''
urlpatterns = patterns('',
  url(r'^$', views.ReferencesList.as_view(), name='reference_list'),
  url(r'^create$', views.ReferenceCreate.as_view(), name='reference_new'),
  url(r'^edit/(?P<pk>\d+)$', views.ReferenceUpdate.as_view(), name='reference_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.ReferenceDelete.as_view(), name='reference_delete'),
)
'''
urlpatterns = patterns('',
    url(r'^$', views.reference_list, name='reference_list'),
    url(r'^create$', views.reference_create, name='reference_new'),
    url(r'^edit/(?P<pk>\d+)$', views.reference_update, name='reference_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.reference_delete, name='reference_delete'),
)
