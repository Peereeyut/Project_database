from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from app_users.form import RegisterForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request, "template.html")

def register(request:HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()



    # medthod GET
    context={"form": form}
    return render(request, "registration/register.html", context)

@login_required
def dashboard(request :HttpRequest):
    return render(request, "registration/dashboard.html")