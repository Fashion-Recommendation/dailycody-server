from django.urls import path
from apps.member.views.info_views import MemberInfo

urlpatterns = [
    path("me/", MemberInfo.as_view())
]

