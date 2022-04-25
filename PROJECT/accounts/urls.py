from django.urls import path
from PROJECT.accounts.views import UserLoginView, UserRegisterView


urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register'),

)
