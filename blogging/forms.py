from django.forms import ModelForm, BooleanField
from blogging.models import Post

class PostForm(ModelForm):
    publish = BooleanField(required=False)
    class Meta:
        model = Post
        fields = ['title', 'body', 'publish',]