from django.db import models
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Transaction, Budget, SavingsGoal
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction, SavingsGoal
from .serializers import (
    CategorySerializer,
    TransactionSerializer,
    BudgetSerializer,
    SavingsGoalSerializer
)
from django.http import JsonResponse

# 🏠 Home endpoint
def home(request):
    return JsonResponse({"message": "Welcome to FinanceMate API 👋"})

# 📁 Categories
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# 💸 Transactions
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# 📊 Budgets
class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# 🎯 Savings Goals
class SavingsGoalViewSet(viewsets.ModelViewSet):
    queryset = SavingsGoal.objects.all()
    serializer_class = SavingsGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        total_transactions = Transaction.objects.filter(user=user).count()
        goals_achieved = SavingsGoal.objects.filter(
            user=user,
            current_amount__gte=models.F('target_amount')
        ).count()

        return Response({
            "total_transactions": total_transactions,
            "goals_achieved": goals_achieved,
        })

