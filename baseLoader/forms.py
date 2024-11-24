from django import forms
from .models import UploadedDB

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDB
        fields = ('file',)
