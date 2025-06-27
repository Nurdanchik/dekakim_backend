from django.urls import path
from feedbacks.views.forms import (
    BuyProductCreateView,
    EmploymentApplicationCreateView,
    FeedbackCreateView
)

urlpatterns = [
    path('buy/', BuyProductCreateView.as_view(), name='buy-product-create'),
    path('employment/', EmploymentApplicationCreateView.as_view(), name='employment-create'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
]