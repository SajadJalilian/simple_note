from django.db import models


class Note(models.Model):
    note_text = models.TextField(max_length=300)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.note_text


class Item(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    item = models.TextField(max_length=300)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.item
