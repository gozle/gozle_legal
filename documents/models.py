from django.db import models
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords

class Language(models.Model):
    class SelectLanguage(models.TextChoices):
        RU = 'ru', 'Ru'
        ENG = 'eng', 'Eng'

    language_name = models.CharField(max_length = 10, choices = SelectLanguage.choices, default = SelectLanguage.RU)

    @classmethod
    def add_language(cls, code, label):
        setattr(cls.SelectLanguage, code.upper(), (code.lower(), label.capitalize()))

    def __str__(self):
        return self.language_name
    
class Category(models.Model):
    title = models.CharField(max_length = 64, unique = True)
    language = models.ForeignKey(Language, related_name = "category_language", on_delete = models.CASCADE)
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
    language = models.ForeignKey(Language, related_name = "document_language", on_delete = models.CASCADE)

    def __str__(self):
        return self.header
    
