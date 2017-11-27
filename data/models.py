from django.db import models


class Data(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    dust25 = models.IntegerField()
    dust100 = models.IntegerField()
    temp = models.FloatField()
    humid = models.IntegerField()
    discomfort_index = models.IntegerField()
    co2 = models.IntegerField()
    device_id = models.CharField(max_length=100)
