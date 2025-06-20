from products.models import Category, Product


def get_all_categories_with_products():
    return Category.objects.prefetch_related('products').all()


def get_product_by_id(product_id: int):
    return Product.objects.select_related('category').prefetch_related('features', 'uses').get(id=product_id)