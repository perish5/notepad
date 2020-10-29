from django import forms
from .models import Note
class NoteFormModel(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ("title","due_date","label")