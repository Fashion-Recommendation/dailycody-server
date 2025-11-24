from django.urls import path
from .views import *

urlpatterns = [
    path("<int:member_id>/", fashion_history_info.as_view()),
    path("", fashion_history_done.as_view())
]
