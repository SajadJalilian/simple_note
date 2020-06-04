from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Note, Item


def note_list(request):
    """
    main view shows all note's in page
    """
    latest_notes = Note.objects.order_by("-pub_date")
    context = {"notes": latest_notes}
    return render(request, "notelist/note_list.html", context)


def note(request, note_id):
    """
    detail page shows a note and it's items
    """
    note = get_object_or_404(Note, pk=note_id)
    latest_items = Item.objects.filter(note__id=note_id).order_by("-pub_date")

    context = {"note": note, "items": latest_items}
    return render(request, "notelist/note_detail.html", context)


def add_note(request):
    """
    page for adding new note
    """
    return HttpResponse("You're looking at add_note")


def item(request, note_id, item_id):
    """
    page show details about an item
    """
    item = get_object_or_404(Item, pk=item_id)
    note = get_object_or_404(Note, pk=note_id)
    context = {"item": item, "note": note}
    return render(request, "notelist/item_detail.html", context)


def add_item(request):
    """
    page for adding new item
    """
    return HttpResponse("You're looking at add_item")
