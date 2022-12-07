from django.db import models

# Create your models here.

class Note(models.Model):
    note_heading = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
   
    def __str__(self):
        return self.note_heading
