from django.contrib import admin
from feedbacks.models.buy_form import BuyProduct
from feedbacks.models.employment import EmploymentApplication
from feedbacks.models.feedback import Feedback

admin.site.register(BuyProduct)
admin.site.register(EmploymentApplication)
admin.site.register(Feedback)   