from django import forms
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    # def save(self):
    #     user = User.objects.first()
    #     self.instance.user = user
    #     return super().save()