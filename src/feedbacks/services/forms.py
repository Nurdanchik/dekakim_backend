from feedbacks.models.employment import EmploymentApplication
from feedbacks.models.feedback import Feedback
from feedbacks.models.buy_form import BuyProduct




def create_buy_product(validated_data):
    return BuyProduct.objects.create(**validated_data)


def create_employment_application(validated_data):
    return EmploymentApplication.objects.create(**validated_data)


def create_feedback(validated_data):
    return Feedback.objects.create(**validated_data)