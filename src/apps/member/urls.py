from django.urls import path
from apps.member.views.info_views import MemberInfo

urlpatterns = [
    path("<int:id>/", MemberInfo.as_view())
]

