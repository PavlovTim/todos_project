# Generated by Django 4.2.1 on 2023-07-10 07:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_alter_todo_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='mod_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='todo',
            name='label',
            field=models.ManyToManyField(blank=True, null=True, to='todos.label'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='parent_todo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todos.todo'),
        ),
    ]