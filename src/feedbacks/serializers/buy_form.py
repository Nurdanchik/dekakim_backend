from rest_framework import serializers
from feedbacks.models.buy_form import BuyProduct


class BuyProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyProduct
        fields = ['name', 'surname', 'phone_number', 'email', 'product']