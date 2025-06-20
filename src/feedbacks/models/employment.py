from django.db import models
from common.models.base import BaseModel


class EmploymentApplication(BaseModel):
    """
    Заявка на трудоустройство
    """

    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        help_text='Например: +996707123456',
        blank=True,
        null=True
    )
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    cv = models.FileField(
        upload_to='media/employees/cvs/',
        verbose_name='Резюме (CV)'
    )
    message = models.TextField(
        verbose_name='Сообщение или сопроводительное письмо',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Заявка на трудоустройство'
        verbose_name_plural = 'Заявки на трудоустройство'