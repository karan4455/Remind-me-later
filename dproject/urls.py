# In urls.py

from django.urls import path
from dapp.views import create_reminder

urlpatterns = [
    path('api/create_reminder/', create_reminder, name='create_reminder'),
]
