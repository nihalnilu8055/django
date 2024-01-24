from django import forms
from web.models import Todo

class Todo_Form(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'