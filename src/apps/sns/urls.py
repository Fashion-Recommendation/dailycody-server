from django.urls import path

from .views.follow_views import SnsPostLike, SnsFollow
from .views.post_views import SnsPostLists
from .views.profile_views import SnsProfile, SnsClosetLists, SnsProfilePosts
from .views.sns_crud_views import SnsPostCreate, SnsPostDetail

urlpatterns = [
    path("posts", SnsPostLists.as_view()),
    path("<int:id>", SnsProfile.as_view()),
    path("<int:id>/posts", SnsProfilePosts.as_view()),
    path("<int:id>/clothes", SnsClosetLists.as_view()),
    path("posts/<int:id>", SnsPostDetail.as_view()),
    path("", SnsPostCreate.as_view()),
    path("posts/<int:post_id>/like", SnsPostLike.as_view()),
    path("follow/<int:user_id>", SnsFollow.as_view()),

]