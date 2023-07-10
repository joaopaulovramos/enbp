from .views import *
from django.conf.urls import url


from django.urls import path

urlpatterns = [
    #path('tasks/', ListTask),
    #url(r'tasks/$', ListTask, name='tasks'),
    url(r'api/tasks/$', ListTask, name='board'),
    path('task/<str:pk>', DetailTask),
]
