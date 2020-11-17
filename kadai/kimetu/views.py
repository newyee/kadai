from django.shortcuts import render, redirect
from .models import Character
from .forms import CharacterForm

# Create your views here.


def index(request):
    return render(request, "kimetu/top.html")


def display(request):
    all_data = Character.objects.all()
    return render(request, "kimetu/display.html", {"all_data": all_data})


def register(request):
    print(request.body)
    params = {"message": "", "form": None}
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/kimetu/display")
        else:
            params["message"] = "再入力して下さい"
            params["form"] = form
    else:
        params["form"] = CharacterForm()
    return render(request, "kimetu/register.html", params)
