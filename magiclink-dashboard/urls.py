from django.urls import path
from .views import ragsearch_view

urlpatterns = [
    path('ragsearch/', ragsearch_view, name='ragsearch'),
]
