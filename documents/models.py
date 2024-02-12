from django.db import models
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords
from .utils import get_language_choices

class Category(models.Model):
    title = models.CharField(max_length = 64, unique = True)

    def __str__(self):
        return self.title


class Document(models.Model):

    class DocumentStatus(models.TextChoices):
        ACTIVE = 'active', 'Active'
        ARCHIVED = 'archived', 'Archived'

    header = models.CharField(max_length = 32)
    body = RichTextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 10, choices = DocumentStatus.choices, default = DocumentStatus.ACTIVE)
    history = HistoricalRecords()

    def __str__(self):
        return self.header