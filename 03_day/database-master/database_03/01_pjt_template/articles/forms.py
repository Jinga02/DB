from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',) # 외래키 필드는 제외하고 출력하기 위해

# 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm작성
class CommentForm(forms.ModelForm):
    
    class Meta:
        model =   Comment
        exclude = ('article',) # 외래 키 필드를 출력에서 제외



