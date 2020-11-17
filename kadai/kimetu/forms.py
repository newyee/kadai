from .models import Character, Gender
from django import forms


class CharacterForm(forms.ModelForm):
    gender = forms.ModelChoiceField(Gender.objects, label="性別")

    class Meta:
        model = Character
        fields = ("name", "gender", "feature")
