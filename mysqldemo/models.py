from django.db import models


# Create your models here.
class Vps(models.Model):
    hostname = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    cpu = models.CharField(max_length=20)

    def __str__(self):
        return self.hostname

    class Meta:
        db_table = 'vps'


