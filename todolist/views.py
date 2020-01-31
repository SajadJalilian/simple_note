from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import Todo, List, Item


def todo_list(request):
    latest_todos = Todo.objects.order_by('-pub_date')
    context = {'todos': latest_todos}
    return render(request, 'todolist/todo_list.html', context)


def todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'todo': todo}
    return render(request, 'todolist/todo_detail.html', context)


def add_todo(request):
    return HttpResponse("You're looking at add_todo")


def item(request, todo_id, item_id):
    item = get_object_or_404(Item, pk=item_id)
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'item': item, 'todo': todo}
    return render(request, 'todolist/item_detail.html', context)

    # return HttpResponse(f"You're looking at item {item_id} and todo {todo_id}")


def add_item(request):
    return HttpResponse("You're looking at add_item")
