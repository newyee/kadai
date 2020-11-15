from django.shortcuts import render
from .models import Character

# Create your views here.


def index(request):
    return render(request, "kimetu/register.html")


def register(request):
    print(request.body)
    if request.method == "POST":
        character_model = Character(
            name=request.POST["name"],
            gender=request.POST["gender"],
            feature=request.POST["feature"],
        )
        character_model.save()
    all_data = Character.objects.all()
    print(all_data)
    return render(request, "kimetu/display.html", {"all_data": all_data})
