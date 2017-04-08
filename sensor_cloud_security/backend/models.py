from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
class Clusters(models.Model):
    operation = models.BooleanField(default=True)
    health = models.CharField(max_length=50, default='unavailable')
    message = models.CharField(max_length=100, default='pending to be deployed', blank=True)
    class Meta:
        ordering = ('id',)


class Sensors(models.Model):
    cluster_id = models.ForeignKey(Clusters, null=False, blank=False, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    sensor_type = models.CharField(max_length=100)
    manufacture = models.CharField(max_length=100)
    operation = models.BooleanField(default=True)
    health = models.CharField(max_length=50, default='unavailable')
    message = models.CharField(max_length=100, default='pending to be deployed', blank=True)

    class Meta:
        ordering = ('id',)
