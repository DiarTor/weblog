from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class EditPostForm(forms.ModelForm, forms.Form):
    title = forms.CharField(max_length=50, required=False)
    content = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = Post
        fields = ["title", "content", "image"]
