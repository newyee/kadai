from django.urls import path
from . import views

app_name = "kimetu"
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("display", views.display, name="display"),
]
