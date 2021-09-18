from django.shortcuts import render
from .models import Project

def home(request):
    # place all items in db.table.project into projects var.
    projects = Project.objects.all()
    # send collected items ( table data ( column, rows )) to the home view.
    return render(request, 'portfolio/home.html', {'projects':projects})
