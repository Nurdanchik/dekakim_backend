from products.models.product import Category, Product, Banner
from django.db.models import Prefetch


def get_all_categories_with_products(language=None):
    if language:
        return Category.objects.prefetch_related(
            Prefetch(
                'products',
                queryset=Product.objects.filter(language=language)
            )
        )
    return Category.objects.prefetch_related('products')


def get_product_by_id(product_id: int):
    return Product.objects.select_related('category').prefetch_related('features', 'uses').get(id=product_id)


def get_products_by_category(category_id: int):
    return Product.objects.filter(category_id=category_id)


def get_category_with_products_by_language(language: str):
    return Category.objects.prefetch_related('products').filter(language=language).first()


def get_banner_by_category_id(category_id: int):
    return Banner.objects.select_related('category').filter(category__id=category_id).first()