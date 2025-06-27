from rest_framework.generics import CreateAPIView
from feedbacks.serializers.buy_form import BuyProductCreateSerializer
from feedbacks.serializers.employment import EmploymentApplicationCreateSerializer
from feedbacks.serializers.feedback import FeedbackCreateSerializer
from feedbacks.services.forms import (
    create_buy_product,
    create_employment_application,
    create_feedback
)


class BuyProductCreateView(CreateAPIView):
    serializer_class = BuyProductCreateSerializer

    def perform_create(self, serializer):
        create_buy_product(serializer.validated_data)


class EmploymentApplicationCreateView(CreateAPIView):
    serializer_class = EmploymentApplicationCreateSerializer

    def perform_create(self, serializer):
        create_employment_application(serializer.validated_data)


class FeedbackCreateView(CreateAPIView):
    serializer_class = FeedbackCreateSerializer

    def perform_create(self, serializer):
        create_feedback(serializer.validated_data)