from django.urls import path
from . import views

urlpatterns = [
    path("", views.note_list, name="note-list"),
    path("<int:note_id>/", views.note, name="note"),
    path("<int:note_id>/<int:item_id>/", views.item, name="item"),
    path("add/note", views.add_note, name="add-note"),
    path("add/item", views.add_item, name="add-item"),
]
