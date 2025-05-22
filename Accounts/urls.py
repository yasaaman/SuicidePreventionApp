from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='user_signup'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLoginView.as_view(), name='user_logout'),
    path('password-reset/', views.PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset/confirm/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('modify/<int:pk>/', views.UserProfileDetailView.as_view(), name='user_infos'),

]


