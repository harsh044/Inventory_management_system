from django.urls import path
from .views import AuthRegister

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('register/', AuthRegister.as_view()),
    
    path('login/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
]
