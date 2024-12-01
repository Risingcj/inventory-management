from django.urls import path
from .views import SalesView

urlpatterns = [
    path('', SalesView.as_view()),  # List and Create Sales
]
