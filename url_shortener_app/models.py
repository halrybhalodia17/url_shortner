from django.db import models

# Create your models here.
class LongToShort(models.Model):
    longurl = models.URLField(max_length=200)
    shorturl = models.CharField(max_length=25, unique=True)
    visit_count=models.IntegerField(default = 1)
    Date = models.DateTimeField(null= True)