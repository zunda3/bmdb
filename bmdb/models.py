from django.db import models

class chartlist(models.Model):
    SONG_ORDER = models.CharField(max_length=200, default='')
    SONG_FAMILY = models.CharField(max_length=200, default='')
    MAIN_TITLE = models.CharField(max_length=200, default='')
    SUB_TITLE = models.CharField(max_length=200, default='')
    PLAYSTYLE = models.CharField(max_length=200, default='')
    MODE = models.CharField(max_length=200, default='')
    TEMPO = models.CharField(max_length=200, default='')
    NOTES = models.CharField(max_length=200, default='')
    CHART_ID = models.CharField(max_length=200, default='')
    DEBUT = models.CharField(max_length=200, default='')
    VERSION = models.CharField(max_length=200, default='')
