from django.shortcuts import render, redirect
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


# 특정 article에 있는 comment 모두 가져온 뒤 context에 추가
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all() # comment_set을 comments로 변경해주었기때문에 comments사용
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:   #
        if request.user == article.user:    # 삭제요청을 한 유저와 글 작성자가 일치하면
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@login_required # 로그인하지 않은 상태에서 접근시 로그인페이지로이동
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user: # 수정 요청 user와 글 작성자가 동일할 시
        print('확인1')
        if request.method == 'POST':
            print('확인2')
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)        
        

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 현재 comment에는 content와 참조한 article값을 넣어줘야함
        # 데이터베이스에 저장되지 않은 인스턴스를 반환
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

