from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'school', 'user')
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     comment = forms.Textarea()
