from django.db import models

# Create your models here.
class Ancestor( models.Model ):
    
    first_name = models.CharField( max_length=25 )
    middle_name = models.CharField( max_length=25, blank=True )
    last_name = models.CharField( max_length=25 )
    birthday = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__( self ):
        return '%s %s' % (self.first_name, self.last_name)

class DocumentType( models.Model ):
    type = models.CharField( max_length=20 )
    create_date = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )

class Document( models.Model ):
    
    document_date = models.DateField()
    document_title = models.CharField( max_length=25 )
    # location is a relative path location
    docuemnt_location = models.CharField( max_length=100 )
    ancestor = models.ForeignKey( Ancestor, on_delete=models.CASCADE )
#    type = models.ForeignKey( DocumentType, on_delete=models.CASCADE )
    create_date = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    
    def __str__( self ):
        return self.document_title

