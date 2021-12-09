from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Comment
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
                            attrs={'class': 'form-control py-4',
                                   'placeholder': 'Введите название статьи'}))

    content = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Post
        fields = ('title', 'content', )
        widgets = {
            'content': SummernoteWidget(),
        }
