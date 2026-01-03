from django.urls import path
from cards.views import index

urlpatterns = [
    path('', index)
    
]