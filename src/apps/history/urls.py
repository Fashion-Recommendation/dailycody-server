from django.urls import path
from .views import *

urlpatterns = [
    path("me/", FashionHistoryInfo.as_view()),
    path("", FashionHistoryDone.as_view())
]
