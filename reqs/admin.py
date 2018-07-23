from django.contrib import admin
from .models import Project,File
from django.urls import reverse

from django.utils.safestring import mark_safe
from django.utils.html import escape
from jet.admin import CompactInline


# Register your models here.


class FileInline(CompactInline):
    model=File
    extra=0
    fields = ('file_name', 'creation_date', 'content')
    

    show_change_link = True
    


class ProjectAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Project Info',{'fields':['project_name','creation_date']}),
        
    ]
    inlines=[FileInline]        
    list_display=('project_name','creation_date')
    list_filter=['creation_date']
    search_fields=['project_name']



admin.site.register(Project,ProjectAdmin)
