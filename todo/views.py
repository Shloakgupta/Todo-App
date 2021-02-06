from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse

def home(request):
    complete = Todo.objects.filter(complete_or_not=True)
    incomplete = Todo.objects.filter(complete_or_not=False)
    stuff_for_frontend = {
        "complete":complete,
        "incomplete":incomplete
    }
    return render(request, "todo/index.html", stuff_for_frontend)

def create(request):
    if request.method == 'POST':
        todo_text = request.POST.get("todo")
        Todo.objects.create(
            text=todo_text,
            complete_or_not=False,
        )
    return redirect('/')
def delete(request, todo_id):
    todo_obj = Todo.objects.get(id=todo_id)
    todo_obj.delete()
    return redirect('/')

def complete(request, todo_id):
    todo_obj = Todo.objects.get(id=todo_id)
    todo_obj.complete_or_not = True
    todo_obj.save()
    return redirect('/')

def undo(request, todo_id):
    todo_obj = Todo.objects.get(id=todo_id)
    todo_obj.complete_or_not = False
    todo_obj.save()
    return redirect('/')

