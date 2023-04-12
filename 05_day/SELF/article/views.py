from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    article = Article.objects.all()
    context = {
        'article' : article
    }
    return render(request, 'article/index.html', context)

def create(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content') 
        # article = Article(title = title, content = content)
        # article.save()
        # ------------------ #
        # ModelForm 사용
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article:detail', article.pk)
        return redirect('article:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'article/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'article/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article:index')

def update(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.title =request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article:detail', pk=article.pk)
    else:
        article = Article.objects.get(pk=pk)
        context = {
            'article' : article
        }
        return render(request, 'article/update.html', context)