from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import todoinf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self):
        txt =super().get_context_data()
        txt["username"] =""
        return txt

class IndexView(TemplateView):
    template_name = "_registration/index.html"

class TodoView(ListView,FilterView):
    model =todoinf
    context_object_name ="tasks"
    template_name = "todo.html"

    def get_queryset(self):
        if self.request.user.is_active:
            return todoinf.objects.filter(userid=self.request.user)
        else:
            return todoinf.objects.none()

class TodoDetail(DetailView):
    model =todoinf
    context_object_name = "detail"
    template_name = "todo_detail.html"

class TodoCreate(LoginRequiredMixin,CreateView):
    model =todoinf
    fields = ['title', 'description','deadline']
    success_url =reverse_lazy("list")
    template_name = "todo_create.html"

    def form_valid(self,form):

        object = form.save(commit=False)
        object.userid = self.request.user
        object.save()
        return super().form_valid(form)

class TodoUpdate(LoginRequiredMixin,UpdateView):
    model =todoinf
    fields = ['title', 'description','deadline']
    success_url =reverse_lazy("list")
    template_name = "todo_create.html"

    def form_valid(self,form):

        object = form.save(commit=False)
        object.userid = self.request.user
        object.save()
        return super().form_valid(form)

class TodoDelete(DeleteView):
    model =todoinf
    context_object_name = "delete"
    success_url =reverse_lazy("list")
    template_name = "todo_delete.html"

class Login(LoginView):
    template_name = "_registration/login.html"

class Logout(LogoutView):
    template_name = "_registration/logout.html"

class PasswordChange(PasswordChangeView):
    template_name = "_registration/password_change_form.html"

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = "_registration/password_change_done.html"

class PasswordReset(PasswordResetView):
    template_name ="_registration/password_reset_form.html"

class PasswordResetDone(PasswordResetDoneView):
    template_name="_registration/password_reset_done.html"
