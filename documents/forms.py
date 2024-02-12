from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Document

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget = CKEditorWidget)
    class Meta:
        model = Document
        fields = ('body',)

class PostForm(forms.Form):
    body = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = Document
        fields = ('body',)