from django.db import models

class chartlist(models.Model):
    SONG_ORDER = models.CharField(max_length=200, default='')
    SONG_FAMILY = models.CharField(max_length=200, default='')
    MAIN_TITLE = models.CharField(max_length=200, default='')
    SUB_TITLE = models.CharField(max_length=200, default='')
    PLAYSTYLE = models.CharField(max_length=10, default='')
    MODE = models.CharField(max_length=10, default='')
    TEMPO = models.CharField(max_length=200, default='')
    NOTES = models.IntegerField(default=0)
    CHART_ID = models.CharField(max_length=8, default='')
    DEBUT = models.CharField(max_length=20, default='')
    VERSION = models.CharField(max_length=20, default='')
