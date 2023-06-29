from django.db import models
from django.db.models import Q


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rate = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)

    def __str__(self):
        return f'Фильм {self.name} был  снят в {self.year} году с бюджетом {self.budget}$ и имеет рейтинг {self.rate}.'



