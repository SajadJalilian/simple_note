from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Todo, List, Item


def todo_list(request):
    # return HttpResponse("You're looking at todo_list")
    latest_todos = Todo.objects.order_by('-pub_date')
    context = {'todos': latest_todos}
    return render(request, 'todolist/todo_list.html', context)


def todo(request, todo_id):
    return HttpResponse("You're looking at todo %s." % todo_id)


def add_todo(request):
    return HttpResponse("You're looking at add_todo")


def item(request, item_id, todo_id):
    return HttpResponse(f"You're looking at item {item_id} and todo {todo_id}")


def add_item(request):
    return HttpResponse("You're looking at add_item")
