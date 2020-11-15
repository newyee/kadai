from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField("名前", max_length=2048)
    gender = models.CharField("性別", max_length=2048)
    feature = models.CharField("特徴", max_length=2048)

    def __str__(self):
        return self.name
