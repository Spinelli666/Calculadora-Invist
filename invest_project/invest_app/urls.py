from django.urls import path
from . import views

urlpatterns = [
    path('investimento/', views.investimento_view, name='investimento'),
]