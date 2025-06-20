from django.urls import path
from products.views.products import (
    CategoryWithProductsListAPIView,
    ProductDetailAPIView,
)

urlpatterns = [
    path('categories/', CategoryWithProductsListAPIView.as_view(), name='category-with-products'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]