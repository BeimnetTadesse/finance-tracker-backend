from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    INCOME = 'IN'
    EXPENSE = 'EX'
    CATEGORY_TYPES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=CATEGORY_TYPES)
    description = models.TextField(blank=True, null=True)
    is_custom = models.BooleanField(default=False)  # True if user-created category
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Only set if custom

    class Meta:
        unique_together = ('name', 'type', 'user')

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
    
from django.db import models
from django.contrib.auth.models import User
from .models import Category

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default='expense')
    is_recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.category} - {self.amount}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    month = models.DateField()  # Store as first of the month (e.g. 2025-08-01)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('user', 'category', 'month')

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.month}"
    

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def progress_percentage(self):
        return (self.current_amount / self.target_amount) * 100 if self.target_amount else 0

    def __str__(self):
        return f"{self.title} ({self.progress_percentage():.0f}%)"

class RecurringTransactionTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    interval = models.CharField(max_length=10, choices=[('MONTHLY', 'Monthly'), ('WEEKLY', 'Weekly')])
    next_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.amount} every {self.interval.lower()}"
