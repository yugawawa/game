from django.urls import path
from . import views 
from .views import HomeView,LoginView,SignupView,TodoView,TodoDetail,TodoCreate,TodoUpdate,TodoDelete
urlpatterns = [
     path("", HomeView.as_view(),),
     path("home/", HomeView.as_view()),
     path("todo/", TodoView.as_view(), name="list"),
     path("detail/<int:pk>", TodoDetail.as_view(), name='detail'), 
     path("create/", TodoCreate.as_view(), name="create"),
     path("update/<int:pk>", TodoUpdate.as_view(), name='update'), 
     path("delete/<int:pk>", TodoDelete.as_view(), name='delete'), 
     path("login/", LoginView.as_view()),
     path("signup/", SignupView.as_view()),
]
