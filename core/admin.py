from django.contrib import admin
from .models import Transaction, Budget, SavingsGoal, RecurringTransactionTemplate, Category

admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(SavingsGoal)
admin.site.register(RecurringTransactionTemplate)
admin.site.register(Category)
