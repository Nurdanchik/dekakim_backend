from products.models.product import Category, Product
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