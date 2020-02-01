from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=20, default=None, null=False)
    note_text = models.TextField(max_length=300, null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Item(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default=None, null=False)
    item_text = models.TextField(null=True, max_length=300)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.name
