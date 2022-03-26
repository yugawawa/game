from django.urls import path
from .views import HomeView
from .views import LoginView
from .views import SignupView
urlpatterns = [
     path("", HomeView.as_view()),
     path("home/", HomeView.as_view()),
     path("login/", LoginView.as_view()),
     path("signup/", SignupView.as_view()),
]
