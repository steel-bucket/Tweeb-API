from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'blog_api'

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('posts/backend', views.PostBackendView.as_view(), name='posts'),
    path('posts/backend/<str:tlink>/', views.SinglePostView.as_view(), name='singlepost'),
]
