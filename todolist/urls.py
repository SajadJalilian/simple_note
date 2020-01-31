from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('<int:todo_id>/', views.todo, name='todo'),
    path('<int:todo_id>/<int:item_id>/', views.item, name='item'),
    path('add/todo', views.add_todo, name='add-todo'),
    path('add/item', views.add_item, name='add-item'),
]
