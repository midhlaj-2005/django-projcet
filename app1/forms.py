from django import forms
from .models import book


class bookform(forms.ModelForm):
     class Meta:
          model =book
          fields=['name','author','price','description']
