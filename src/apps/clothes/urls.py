from django.urls import path
from .views import *

urlpatterns = [
    path("<int:id>/", ClosetInfo.as_view()),
    path("", RegisterClothes.as_view())
]
