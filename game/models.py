from django.db import models

class Level(models.Model):
    name = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Player(models.Model):
    login = models.CharField(max_length = 125)
    nb_stars = models.IntegerField()            #min & max
    time = models.IntegerField()
    id_level = models.ForeignKey('Level' ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.login

class Detail(models.Model):
    image = models.CharField(max_length = 255)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    id_level = models.ForeignKey('Level' ,on_delete=models.CASCADE)

