from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
#    imdb_rating = models.FloatField()
#    poster_url = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.title} from {self.year}'
