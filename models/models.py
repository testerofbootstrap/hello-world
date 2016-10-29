from django.db import models

# Create your models here.


class data_locality(models.Model):
    name                        = models.CharField(max_length=200)
    description                 = models.CharField(max_length=200)
    slug                        = models.SlugField(unique=True)
    comment                     = models.TextField(blank=True)
    image                       = models.ImageField(upload_to="images/beerthumbs/", blank=True)
    def __str__(self):
            return '%s %s' % (self.name, self.description)


class Brewery(models.Model):
    name            = models.CharField(max_length=200)
    slug            = models.SlugField(unique=True)
    description     = models.TextField(blank=True)

    def __str__(self):
            return '%s %s' % (self.name, self.description)