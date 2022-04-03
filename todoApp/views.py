from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from .models import todoinf
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self):
        txt =super().get_context_data()
        txt["username"] =""
        return txt
class Login(LoginView):
    template_name = "registration/_login.html"

class IndexView(TemplateView):
    template_name = "registration/index.html"

class TodoView(ListView):
    model =todoinf
    context_object_name ="tasks"
    template_name = "todo.html"

class TodoDetail(DetailView):
    model =todoinf
    context_object_name = "detail"
    template_name = "todo_detail.html"

class TodoCreate(CreateView):
    model =todoinf
    fields = ['title', 'description','deadline']
    success_url =reverse_lazy("list")
    template_name = "todo_create.html"

class TodoUpdate(UpdateView):
    model =todoinf
    fields = ['title', 'description','deadline']
    success_url =reverse_lazy("list")
    template_name = "todo_create.html"

class TodoDelete(DeleteView):
    model =todoinf
    context_object_name = "delete"
    success_url =reverse_lazy("list")
    template_name = "todo_delete.html"
