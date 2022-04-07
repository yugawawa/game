from django.urls import path,include
from . import views 
from .views import HomeView,TodoView,TodoDetail,IndexView
from .views import TodoCreate,TodoUpdate,TodoDelete,Login,Logout
from .views import PasswordChange,PasswordChangeDone,PasswordReset,PasswordResetDone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
urlpatterns = [
     path("", login_required(IndexView.as_view()),name="index"),
     path('login/', Login.as_view(), name="login"),
     path('logout/', Logout.as_view(), name="logout"), 
     path('password_change/', PasswordChange.as_view(), name="password_change"), 
     path('password_change/done', PasswordChangeDone.as_view(), name="password_change_done"), 
     path('password_reset/', PasswordReset.as_view(), name="password_reset"), 
     path('password_reset/done', PasswordResetDone.as_view(), name="password_reset_done"), 
     path("home/", login_required(HomeView.as_view())),
     path("todo/", login_required(TodoView.as_view()), name="list"),
     path("detail/<int:pk>", login_required(TodoDetail.as_view()), name='detail'), 
     path("create/", login_required(TodoCreate.as_view()), name="create"),
     path("update/<int:pk>", login_required(TodoUpdate.as_view()), name='update'), 
     path("delete/<int:pk>", login_required(TodoDelete.as_view()), name='delete'), 

]
