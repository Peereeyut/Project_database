from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from app_users.form import ExtendedProfileForm, RegisterForm, Userprofile
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

@login_required
def profile(request:HttpRequest):
    user = request.user
    if request.method == 'POST':
        form = Userprofile(request.POST, instance=user)#การใส่ instanceจะเป็นการใช้updateไม่ใช่insert
        is_new_profile=False
        try:#update
            extend_form = ExtendedProfileForm(request.POST, instance=user.profile)
        except:#create
            extend_form = ExtendedProfileForm(request.POST)
            is_new_profile=True


        if form.is_valid() and extend_form.is_valid():
            form.save()
            if is_new_profile:#create
                profile=extend_form.save(commit=False)
                profile.user = user
                profile.save()
            else:#update
                extend_form.save()
            return HttpResponseRedirect(reverse('profile'))

    else:
        form=Userprofile(instance=user)
        try:
            extend_form=ExtendedProfileForm(instance=user.profile)
        except:
            extend_form=ExtendedProfileForm()


    #Get
    # form = Userprofile()
    # extend_form = ExtendedProfileForm()
    context={
        "form":form,
        "ex":extend_form
    }

    return render(request, "registration/profile.html", context)


def course(request):
    return render(request, "registration/course.html")