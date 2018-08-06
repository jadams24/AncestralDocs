'''
Created on Jul 23, 2018

@author: jadams24
'''

from django.urls import path, re_path
from django.views.generic import ListView
from people.models import Ancestor, Document
from . import views
from people.views import DocumentListView, DocumentView

urlpatterns = [
    path( '', views.index, name='index' ),
    re_path(r'^people/$', 
        ListView.as_view( queryset=Ancestor.objects.all().order_by( "last_name" )[:25], template_name="people/people.html" )),
    re_path( r'^people/documentview', DocumentListView.as_view()),
#    re_path(r'^people/static/people/documents/', views.pdf_view, name='pdf_view' ),
    re_path( r'^people/static/people/documents/', DocumentView.as_view() ),
]
