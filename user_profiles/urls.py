from django.conf.urls import include, url
from django.urls import path, re_path
from django.contrib import admin
from api.views import *
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', UserAuthentication.as_view(), name='UserAuthenticationAPI'),
    path('api/logout/', Logout.as_view()),
    path('api/register/', Register.as_view()),
    path('api/profile/', Profiles.as_view()),
    path('api/all_profiles/', AllProfiles.as_view()),
    path('api/add_friend/', AddFriend.as_view()),
    path('api/delete_friend/', DeleteFriend.as_view()),
    re_path(r'^search/(?:gender-(?P<gender>\d+)/)?$',ProfileSearch.as_view()), 
    re_path(r'^search/(?:city-(?P<city>\d+)/)?$',ProfileSearch.as_view()),    
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
