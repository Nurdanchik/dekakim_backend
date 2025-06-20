from django.db import models
from common.models.base import BaseModel


class Category(BaseModel):
    """
    Категория продукта
    """

    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(BaseModel):
    """
    Продукт
    """

    face_img = models.ImageField(
        upload_to='media/cards/faces/',
        verbose_name='Главное фото'
    )
    slogan = models.TextField(verbose_name='Слоган')
    product_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название продукта'
    )
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Use(BaseModel):
    """
    Область применения продукта
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='uses',
        verbose_name='Продукт'
    )
    text = models.TextField(verbose_name='Описание применения')

    def __str__(self):
        return f"Применение: {self.product.product_name}"

    class Meta:
        verbose_name = 'Область применения'
        verbose_name_plural = 'Области применения'


class Feature(BaseModel):
    """
    Особенность продукта
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='features',
        verbose_name='Продукт'
    )
    text = models.TextField(verbose_name='Особенность')

    def __str__(self):
        return f"Особенность: {self.product.product_name}"

    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'




# from django.db import models
# from common.models.base import BaseModel
#
#
# class Category(BaseModel):
#     """
#     Название категории:
#
#     Аттрибуты:
#     -name: название категории
#     """
#
#     name = models.CharField(
#         max_length=100, unique=True,
#         verbose_name='Название категории')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#
#
# class Product(BaseModel):
#     """
#     Продукты:
#
#     Аттрибуты:
#     -product_name: название продукта
#     """
#
#     face_img = models.ImageField(
#         upload_to='media/cards/faces/',
#         verbose_name='Главное фото'
#     )
#     slogan = models.TextField(
#         verbose_name='Слоган'
#     )
#     product_name = models.CharField(
#         max_length=100,
#         unique=True,
#         verbose_name='Название продукта')
#     description = models.TextField(
#         verbose_name='Описание'
#     )
#
#     def __str__(self):
#         return self.product_name
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'
#
#
#
# class Use(BaseModel):
#     """
#     Продукты:
#
#     Аттрибуты:
#     -product_name: название продукта
#     """
#
#     product_name = models.CharField(max_length=100, unique=True, verbose_name='Название продукта')
#
#     def __str__(self):
#         return self.product_name
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'
#
#
# class Feature(BaseModel):
#     """
#     Продукты:
#
#     Аттрибуты:
#     -product_name: название продукта
#     """
#
#     product_name = models.CharField(max_length=100, unique=True, verbose_name='Название продукта')
#
#     def __str__(self):
#         return self.product_name
#
#     class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'