from django.urls import path
from .views import *

urlpatterns = [
    path("posts", ShopPostLists.as_view()),
    path("posts/<int:id>", ShopPostDetail.as_view()),
    path("orders", ShopPostOrder.as_view())
]