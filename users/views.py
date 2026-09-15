from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})

class Login(LoginView):
    template_name = "users/login.html"

@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")

