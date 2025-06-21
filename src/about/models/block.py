from django.db import models
from common.models.base import BaseModel


class Block(BaseModel):
    """
    Блок на сайте
    """
    BLOCKTYPES = (
        ('About us', 'About us'),
        ('Our vision', 'Our vision'),
        ('Our mission', 'Our mission'),
        ('Res. & Dev.', 'Res. & Dev'),
    )
    LANGUAGES = (
        ('Eng', 'English'),
        ('Tur', 'Turkish'),
    )

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название поста'
    )
    blocktype = models.CharField(
        max_length=10,
        choices=BLOCKTYPES,
        verbose_name='Тип блока'
    )
    language = models.CharField(
        max_length=10,
        choices=LANGUAGES,
        default='Eng',
        verbose_name='Выбор языка'
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Блок на сайте'
        verbose_name_plural = 'Блоки на сайте'


class BlockPhoto(BaseModel):
    """
    Фото блока на сайте
    """

    post = models.ForeignKey(
        Block, on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='Блок'
    )
    photo = models.ImageField(
        upload_to='media/blocks/photos/',
        verbose_name='Фото'
    )

    class Meta:
        verbose_name = 'Фото блока'
        verbose_name_plural = 'Фото блока'


class BlockVideo(BaseModel):
    """
    Видео блока на сайте
    """

    post = models.ForeignKey(
        Block, on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='Блок'
    )
    video = models.FileField(
        upload_to='media/blocks/videos',
        verbose_name='Видео'
    )

    class Meta:
        verbose_name = 'Видео блока'
        verbose_name_plural = 'Видео блока'