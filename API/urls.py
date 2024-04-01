from django.contrib import admin
from django.urls import path, include
from google.views import GoogleView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('RestAPI.urls', namespace='RestAPI')),
    path('api/users/', include('Auth.urls', namespace='Auth')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('google/', GoogleView.as_view(), name='google'),  # add path for google authentication
]
