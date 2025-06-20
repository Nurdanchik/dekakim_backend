from rest_framework import serializers
from products.models import Product, Category, Feature, Use


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'text']


class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Use
        fields = ['id', 'text']


class ProductSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)
    uses = UseSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            'id',
            'face_img',
            'slogan',
            'product_name',
            'description',
            'category',
            'features',
            'uses',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']