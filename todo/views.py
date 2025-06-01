from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def index(request):
    # Only show todos for the logged-in user
    todos = Todo.objects.filter(user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title, user=request.user)
        return redirect('/')
    return render(request, 'index.html', {'todos': todos})

@login_required
def complete(request, todo_id):
    # Only allow users to complete their own todos
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.completed = True
    todo.save()
    return redirect('/')

@login_required
def delete(request, todo_id):
    # Only allow users to delete their own todos
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect('/')
