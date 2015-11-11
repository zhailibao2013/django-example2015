__author__ = 'zhailb'
from django.conf.urls import include, url
from views import dashboard,edit,detail,add,delete
urlpatterns = [
    url(r'^$', dashboard,name="host_index"),
    url(r'edit/(?P<host_id>\d+)', edit, name="host_edit"),
    url(r'detail/(?P<host_id>\d+)', detail, name="host_detail"),
    url(r'add', add),
    url(r'delete/(?P<host_id>\d+)', delete, name="host_delete"),
]

