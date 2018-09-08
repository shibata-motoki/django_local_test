from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todo_list = Todo.objects.all()
    return render(
        request, 'todo/todo_list.html', {'todo_list': todo_list})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(
        request, 'todo/todo_detail.html', {'todo': todo})

def todo_add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('todo:todo_detail', pk=post.pk)
    else:
        form = TodoForm()
    return render(request, 'todo/todo_edit.html', {'form': form})


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('todo:todo_detail', pk=post.pk)
    else:
        form = PostFrom(instance=post)
    return render(request, 'todo/todo_edit.html', {'form': form})


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect(request, 'todo:todo_list')
    return render(request, 'todo/todo_delete.html', {'todo': todo})
