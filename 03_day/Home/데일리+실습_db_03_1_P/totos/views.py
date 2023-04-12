from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods
from .models import Todo
from .forms import TodoForm

# Create your views here.
@require_safe
def index(request):
    if request.user.is_authenticated == False:
        return redirect('accounts:login')
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todos/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.user.is_authenticated == False:
        return redirect('accounts:login')
    # POST : form 데이터를 받아와서 TODO를 생성
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # 해당되는 todo 저장
            todo  = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todo:index')
    # GET : 입력폼을 주게하는
    else:
        form = TodoForm()
    
    context = {
        'form' : form,
    }
    return render(request, 'todos/create.html', context)