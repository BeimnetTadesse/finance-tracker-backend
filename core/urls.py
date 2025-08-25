from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserStatsView
from .views import (
    CategoryViewSet,
    TransactionViewSet,
    BudgetViewSet,
    SavingsGoalViewSet,
    home
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'budgets', BudgetViewSet, basename='budget')
router.register(r'goals', SavingsGoalViewSet, basename='goal')

urlpatterns = [
    path('', home),  # Optional root endpoint
    path('stats/', UserStatsView.as_view(), name='user-stats'),
]

urlpatterns += router.urls
