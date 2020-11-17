from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ("男", "男"),
    ("女", "女"),
)


class Character(models.Model):
    name = models.CharField("名前", max_length=2048)
    gender = models.CharField("性別", choices=GENDER_CHOICES, max_length=250)
    feature = models.CharField("特徴", max_length=2048)

    def __str__(self):
        return self.name


class Gender(models.Model):
    gender = models.CharField("性別", choices=GENDER_CHOICES, max_length=250)

    def __str__(self):
        return self.gender
