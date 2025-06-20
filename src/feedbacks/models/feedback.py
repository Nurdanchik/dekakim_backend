from django.db import models
from common.models.base import BaseModel


class Feedback(BaseModel):
    """
    Обратная связь от пользователя
    """

    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f"Отзыв от {self.name}"

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'