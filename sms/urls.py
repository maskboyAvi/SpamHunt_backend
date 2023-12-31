from django.urls import include, path
from .views import *

urlpatterns = [
    path('', SmsView.as_view()),
]