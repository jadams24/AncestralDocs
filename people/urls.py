'''
Created on Jul 23, 2018

@author: jadams24
'''

from django.urls import path, re_path
from django.views.generic import ListView
from people.models import Ancestor
from . import views

urlpatterns = [
    path( '', views.index, name='index' ),
    re_path(r'^people/', 
         ListView.as_view( queryset=Ancestor.objects.all().order_by( "last_name" )[:25], template_name="people/people.html" )),
]
