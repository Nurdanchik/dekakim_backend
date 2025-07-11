# Generated by Django 5.2.3 on 2025-06-24 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Block",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Название поста"
                    ),
                ),
                (
                    "blocktype",
                    models.CharField(
                        choices=[
                            ("About us", "About us"),
                            ("Our vision", "Our vision"),
                            ("Our mission", "Our mission"),
                            ("Res. & Dev.", "Res. & Dev"),
                        ],
                        max_length=20,
                        verbose_name="Тип блока",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("Eng", "English"), ("Tur", "Turkish")],
                        default="Eng",
                        max_length=10,
                        verbose_name="Выбор языка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блок на сайте",
                "verbose_name_plural": "Блоки на сайте",
            },
        ),
        migrations.CreateModel(
            name="BlockPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "photo",
                    models.ImageField(upload_to="blocks/photos/", verbose_name="Фото"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="about.block",
                        verbose_name="Блок",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото блока",
                "verbose_name_plural": "Фото блока",
            },
        ),
        migrations.CreateModel(
            name="BlockVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "video",
                    models.FileField(upload_to="blocks/videos/", verbose_name="Видео"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="about.block",
                        verbose_name="Блок",
                    ),
                ),
            ],
            options={
                "verbose_name": "Видео блока",
                "verbose_name_plural": "Видео блока",
            },
        ),
    ]
