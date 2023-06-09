from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == "GET":
        return render(
            request, "home/register.html",
            {"form": CustomUserCreationForm}
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home/index.html"))
