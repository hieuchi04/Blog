from django import forms
from .models import PostModel

class PostModelForm(forms.ModelForm):
    #cho ô content chỉ hiện thị 3 hàng
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model = PostModel
        fields = ('title', 'content')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')