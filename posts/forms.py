from django import forms
from .models import post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('__all__')


class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model = Comment
        fields = ('content', )