from django.db import models

# create class, class will represent the table,columns within the db
# every project will have the below features.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    date = models.DateField()
