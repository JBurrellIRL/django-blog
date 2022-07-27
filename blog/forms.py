from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Comment important as Python needs to see this as a tuple 
        fields = ('body',)
