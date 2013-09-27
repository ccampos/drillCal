from django.db import models

class Day(models.Model):
    exercise_type = models.CharField(max_length=30)
    exert_percent = models.IntegerField(default=85)
