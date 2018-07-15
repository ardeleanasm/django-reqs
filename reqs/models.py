from django.db import models
from django.utils import timezone
import datetime
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from django.template.defaultfilters import escape


# Create your models here.
class Project(models.Model):
    project_name=models.CharField(max_length=512)
    creation_date=models.DateTimeField('date created')
    
    def __str__(self):
        return self.project_name
    
    def was_created_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.creation_date <= now
    was_created_recently.admin_order_field = 'creation_date'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'


class File(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    file_name=models.CharField(max_length=512,default="NewFile")
    creation_date=models.DateTimeField('date created')
    content=MarkdownxField(default="")
    def __str__(self):
        return self.file_name

    @property
    def formatted_markdown(self):
        return markdownify(self.content)


####
# class FileAuthors(models.Model):
#     file=models.ForeignKey(File,on_delete=models.CASCADe)

