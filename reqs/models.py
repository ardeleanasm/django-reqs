from django.db import models
from django.utils import timezone
import datetime
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import base64
from django.template.defaultfilters import escape

#fields

# class Base64Field(models.TextField):

#     def contribute_to_class(self,cls,name):
#         if self.db_column is None:
#             self.db_column=name
#         self.field_name = name + '_base64'
#         super(Base64Field, self).contribute_to_class(cls, self.field_name)
#         setattr(cls, name, property(self.get_data, self.set_data))
    
#     def get_data(self, obj):
#         return base64.decodestring(getattr(obj, self.field_name))

#     def set_data(self, obj, data):
#         setattr(obj, self.field_name, base64.encodestring(data))

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

class FileObjects(models.Model):
    file=models.ForeignKey(File,on_delete=models.CASCADE)
    object_name=models.CharField(max_length=512,default="")
    _data=models.BinaryField()
    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)

####
# class FileAuthors(models.Model):
#     file=models.ForeignKey(File,on_delete=models.CASCADe)

