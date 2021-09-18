from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    # give a total of 5 objs and order by date in decending order, ( give most recent articles )
    # similar to paginating or grouping or chunking the results of the query.
    blogs = Blog.objects.all().order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
