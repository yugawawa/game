from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self):
        txt =super().get_context_data()
        txt["username"] =""
        return txt

class LoginView(TemplateView):
    template_name = "login.html"

class SignupView(TemplateView):
    template_name = "signup.html"