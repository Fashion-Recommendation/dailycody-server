from django.urls import path
from .views import *

urlpatterns = [
    path("<int:member_id>/", FashionHistoryInfo.as_view()),
    path("", FashionHistoryDone.as_view())
]
