from django.db import models
from common.models.base import BaseModel
from products.models.product import Product


class BuyProduct(BaseModel):
    """
    Product purchase request
    """

    name = models.CharField(max_length=100, verbose_name='First name')
    surname = models.CharField(max_length=100, verbose_name='Last name')
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Phone number',
        help_text='Example: +996707123456',
        blank=True,
        null=True
    )
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_to_buy',
        verbose_name='Product'
    )

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Product purchase request'
        verbose_name_plural = 'Product purchase requests'