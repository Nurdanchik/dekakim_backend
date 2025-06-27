from django.db import models
from common.models.base import BaseModel


class Feedback(BaseModel):
    """
    User feedback
    """

    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f"Feedback from {self.name}"

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'