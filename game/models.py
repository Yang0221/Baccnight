from django.db import models

class Level(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField() 

    def __str__(self):
        return self.title
    
class Player(models.Model):
    login = models.CharField(max_length = 125)
    nb_stars = models.IntegerField()            #min & max
    time = models.TimeField()
    id_level = models.ForeignKey('Level' , models.CASCADE)
