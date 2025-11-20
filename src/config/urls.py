from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cloth/', include('apps.cloth.urls')),
    path('member/', include('apps.member.urls')),
    path('recommend/', include('apps.recommend.urls')),
    path('shop/', include('apps.shop.urls')),
    path('sns/', include('apps.sns.urls')),
]
