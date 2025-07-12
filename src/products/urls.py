from django.urls import path
from products.views.products import (
    CategoryWithProductsListAPIView,
    ProductDetailAPIView,
    ProductCardsByCategoryView,
    CategoryCardsByLanguageView, 
    BannerByCategoryView
)

urlpatterns = [
    path('categories/', CategoryWithProductsListAPIView.as_view(), name='category-with-products'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:category_id>/cards/', ProductCardsByCategoryView.as_view(), name='category-product-cards'),
    path('category/cards/', CategoryCardsByLanguageView.as_view(), name='category-cards-by-language'),
    path('banner/', BannerByCategoryView.as_view(), name='category-banner'),
]