from django.urls import path
from src.apps.member.views.info_views import *

urlpatterns = [
    path("<int:id>/", member_info.as_view())
]

