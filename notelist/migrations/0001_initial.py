# Generated by Django 3.0.7 on 2020-06-04 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.TextField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notelist.Note')),
            ],
        ),
    ]
