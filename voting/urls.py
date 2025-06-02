from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
    path('finalVote/', views.finalVote, name='finalVote'),
   # path('voteSuccess/', views.voteSuccess, name='voteSuccess'),
]
