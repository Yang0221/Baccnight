from django.db import models

class Level(models.Model):
    name = models.CharField(max_length = 255)
    image = models.TextField()
    id_world = models.ForeignKey('World' , models.CASCADE)

    def __str__(self):
        return self.title


class Player(models.Model):
    login = models.CharField(max_length = 125, primary_key=True)
    nb_stars = models.IntegerField()            #min & max
    time = models.TimeField()
    id_level = models.ForeignKey('Level' , models.CASCADE)

    def __str__(self):
        return self.login


class World(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name



class Clue(models.Model):
    description = models.TextField()
    id_level = models.ForeignKey('Level' , models.CASCADE)

    def __str__(self):
        return self.name


class Detail(models.Model):
    image = models.TextField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    id_level = models.ForeignKey('Level' , models.CASCADE)

    def __str__(self):
        return self.image
