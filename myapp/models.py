from django.db import models

class ThyroidRecord(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    tsh = models.FloatField()
    t3 = models.FloatField()
    t4 = models.FloatField()
    thyroid_meds = models.BooleanField()
    prediction = models.CharField(max_length=20)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.prediction}"
