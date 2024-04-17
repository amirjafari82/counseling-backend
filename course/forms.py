from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder':'دیدگاه شما','id':'course-comment-textarea'})
        }