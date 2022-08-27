# Generated by Django 3.2.15 on 2022-08-27 16:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("todoapp", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="author"
            ),
        ),
        migrations.AddField(
            model_name="todo",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="todoapp.project", verbose_name="project"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
