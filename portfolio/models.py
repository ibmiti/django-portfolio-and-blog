from django.db import models

# create class, class will represent the table,columns within the db
# every project will have the below features.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
