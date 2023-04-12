from django import forms
from .models import Article
class ArticleForm(forms.Form):
    # title = forms.CharField(max_length=30)
    # content = forms.CharField()
    class Meta:
        model = Article
        fields = '__all__'