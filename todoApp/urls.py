from django.urls import path,include
from . import views 
from .views import HomeView,TodoView,TodoDetail,IndexView
from .views import TodoCreate,TodoUpdate,TodoDelete,Login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
urlpatterns = [
     path("", login_required(IndexView.as_view()),name="index"),
     path('login/', Login.as_view(), name="login"),#ログインページへのパス
     path("home/", HomeView.as_view()),
     path("todo/", TodoView.as_view(), name="list"),
     path("detail/<int:pk>", TodoDetail.as_view(), name='detail'), 
     path("create/", TodoCreate.as_view(), name="create"),
     path("update/<int:pk>", TodoUpdate.as_view(), name='update'), 
     path("delete/<int:pk>", TodoDelete.as_view(), name='delete'), 

]
