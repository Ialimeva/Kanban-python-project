from django.db import models
from django.utils.timezone import now

class Tasklist(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField(default = now)
    finish_date = models.DateTimeField(default = now)
