from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=120)
    roll = models.IntegerField()
    reg = models.IntegerField()
    marks = models.IntegerField()

    def __str__(self):
        return self.name
