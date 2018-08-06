from django.contrib import admin
from .models import Ancestor, Document, DocumentType

# Register your models here.

admin.site.register( Ancestor )
admin.site.register( Document )
admin.site.register( DocumentType )