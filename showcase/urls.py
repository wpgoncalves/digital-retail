from django.urls import path
from showcase import views

urlpatterns = [
    path('', views.showcase, name='showcase'),
    path('valida_newsletter/', views.valida_newsletter, name='valida_newsletter'),
]
