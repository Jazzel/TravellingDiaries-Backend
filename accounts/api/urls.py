from django.urls import path,include

from .views import (ProfilesListApiView,HelloView,GetUserProfileListApiView)
app_name = 'accounts-api'
urlpatterns = [
    path('', ProfilesListApiView.as_view(), name='list'),
    path('user-info/', GetUserProfileListApiView.as_view(), name='user-info'),
    path('rest-auth/', include('rest_auth.urls')),

]
