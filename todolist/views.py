from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import Todo, Item


def todo_list(request):
    """
    main view shows all todo's in page
    """
    latest_todos = Todo.objects.order_by('-pub_date')
    context = {'todos': latest_todos}
    return render(request, 'todolist/todo_list.html', context)



def todo(request, todo_id):
    """
    detail page shows a todo and it's items
    """
    todo = get_object_or_404(Todo, pk=todo_id)
    latest_items = Item.objects.filter(todo__id=todo_id).order_by('-pub_date')

    context = {'todo': todo, 'items': latest_items}
    return render(request, 'todolist/todo_detail.html', context)



def add_todo(request):
    """
    page for adding new todo
    """
    return HttpResponse("You're looking at add_todo")



def item(request, todo_id, item_id):
    """
    page show details about an item
    """
    item = get_object_or_404(Item, pk=item_id)
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'item': item, 'todo': todo}
    return render(request, 'todolist/item_detail.html', context)


def add_item(request):
    """
    page for adding new item
    """
    return HttpResponse("You're looking at add_item")
