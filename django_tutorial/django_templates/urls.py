from django.urls import path
from . import views

urlpatterns = [
    path('humanize/', views.view_humanize, name="humanize" ),
]