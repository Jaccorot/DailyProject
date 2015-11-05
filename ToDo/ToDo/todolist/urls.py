from django.conf.urls import include, url

urlpatterns = [
    url(r'^(\d+)/$', 'todolist.views.view_list', name='view_list'),
    url(r'^new$', 'todolist.views.new_list', name='new_list'),
]
