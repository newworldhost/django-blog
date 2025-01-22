from .models import Comment
from django import forms

class CommentForm(forms.model.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)