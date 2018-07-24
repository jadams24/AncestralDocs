from django.db import models

# Create your models here.
class Ancestor( models.Model ):
    
    first_name = models.CharField( max_length=50 )
    last_name = models.CharField( max_length=50 )
    birthday = models.DateTimeField()
    last_modified = models.DateTimeField()

    def __str__( self ):
        return '%s %s' % (self.first_name, self.last_name)
