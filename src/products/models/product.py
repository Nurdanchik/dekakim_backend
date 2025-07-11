from django.db import models
from common.models.base import BaseModel


class Category(BaseModel):
    """
    Product category
    """

    logo = models.ImageField(
        upload_to='categories/logos/',
        verbose_name='Category logo'
    )
    name = models.CharField(max_length=100, unique=True, verbose_name='Category name')
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    """
    Product
    """

    LANGUAGES = (
        ('Eng', 'English'),
        ('Tur', 'Turkish'),
    )

    language = models.CharField(
        max_length=10,
        choices=LANGUAGES,
        default='Eng',
        verbose_name='Language'
    )
    face_img = models.ImageField(
        upload_to='cards/faces/',
        verbose_name='Main photo'
    )
    slogan = models.TextField(verbose_name='Slogan')
    code = models.CharField(
        max_length=20,
        verbose_name='Product code'
    )
    subcode = models.CharField(
        max_length=20,
        verbose_name='Product subcode'
    )
    product_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Product name'
    )
    description = models.TextField(verbose_name='Description')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Category'
    )

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Use(BaseModel):
    """
    Product use case
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='uses',
        verbose_name='Product'
    )
    text = models.TextField(verbose_name='Use case description')

    def __str__(self):
        return f"Use case: {self.product.product_name}"

    class Meta:
        verbose_name = 'Use case'
        verbose_name_plural = 'Use cases'


class Feature(BaseModel):
    """
    Product feature
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='features',
        verbose_name='Product'
    )
    text = models.TextField(verbose_name='Feature')

    def __str__(self):
        return f"Feature: {self.product.product_name}"

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'