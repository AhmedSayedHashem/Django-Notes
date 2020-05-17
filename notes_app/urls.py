from django.conf.urls import url
from . import views
# this app_name to use namespace
app_name='note_app'
urlpatterns=[
    url(r'^$', views.all_notes, name='all_notes'),
    # url(r'^(?P<id>\d+)$', views.details, name='note_details')
    url(r'^(?P<slug>[-\w]+)/$', views.details, name='note_details'),
    url(r'^add$', views.note_add, name='add_note'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit, name='note_edit'),


]