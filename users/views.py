from django.contrib.auth import login
from users.forms import CustomUserCreationForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.shortcuts import render


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home:index")
