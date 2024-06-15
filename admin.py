from django.contrib import admin
from.models import *
# Register your models here.
@admin.register(Signup)
class Signupadmin(admin.ModelAdmin):
    list_display=['user','contact','year','stream','role','roll']
@admin.register(Notes)
class Notesadmin(admin.ModelAdmin):
    list_display=['user','uploadingdate','stream','year','subject','notesfile','filetype','description','status']