from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, RedirectView
from people.models import Document

# import urllib

# Create your views here.

def index( request ):
    return render(request, 'people/home.html')

def pdf_view(request):
    path_seperator = '/'
    pdf = request.path_info
    lst = pdf.split(path_seperator)
    
    pdf = ''
    
    for x in range(2, len(lst)):
        pdf = pdf + lst[x] + path_seperator
    
    pdf = pdf[:-1]
    filename = lst[len(lst)-1][:-4]
    
    response = HttpResponse(pdf, "application/pdf")
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
        
    return response

# def output_file(request, file, mimetype):
#     f = urllib.urlopen(file)
#     data = f.read()
#     f.close()
#     return HttpResponse(data, mimetype=mimetype)

class DocumentView( RedirectView ):
    
    def get_redirect_url(self, *args, **kwargs):
        pdf = self.request.path_info
        url = 'static/people/documents/LetterToFerdinandWalker-18620710.pdf'
        return super().get_redirect_url(*args, **kwargs) 

# class DocumentView( View ):
#     
#     def get( self, request ):
#         return super( DocumentView, self ).get( request ) 

class DocumentListView( ListView ):
    ancestor_id = -1
    template_name = 'people/document-list.html'
    context_object_name = 'document'
    
    def get( self, request ):
        self.ancestor_id = request.GET['id']
        return super( DocumentListView, self ).get( request )
        
    def get_queryset(self):
        
        return Document.objects.filter( ancestor = self.ancestor_id )   #ListView.get_queryset(self)




