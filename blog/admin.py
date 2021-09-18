from django.contrib import admin
from .models import Blog

# Register ( or import models here ) your models here.
    # this allows for the models items to be accessible to the admin panel
        # example : if I add pictures or other media to the model ( or db.table ) then I am effectively allowing
        # the admin panel to have access, or call the objects/items from the db.table ( model )

# project model sent to admin panel
admin.site.register(Blog)
