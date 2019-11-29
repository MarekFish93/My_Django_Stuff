from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete  = models.PROTECT)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)


    def __str__(self):
        return self.name

class AccesRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete  = models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
