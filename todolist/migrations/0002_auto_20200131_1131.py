# Generated by Django 3.0.2 on 2020-01-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_text',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='note_text',
            field=models.TextField(max_length=300, null=True),
        ),
    ]