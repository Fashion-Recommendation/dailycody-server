from django.urls import path
from .views import *

urlpatterns = [
    path("<int:member_id>/", closet_info.as_view())
]
