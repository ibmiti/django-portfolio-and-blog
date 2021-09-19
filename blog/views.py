from django.shortcuts import render, get_object_or_404
from .models import Blog

#  a view is similar to a controller ( mvc )

def all_blogs(request):
    # get number of blogs written
    blog_count = Blog.objects.count
    # give a total of 5 objs and order by date in decending order, ( give most recent articles )
    # similar to paginating or grouping or chunking the results of the query.
    blogs = Blog.objects.all().order_by('-date')

    # ex : of getting only 5 of most recent
    # blogs = Blog.objects.all().order_by('-date')[:5]

    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'blog_count':blog_count})

# get specified blog, by the blog id and request
def detail(request, blog_id):
    # build the error message or success, store within the blog var
    # pk == primary key, for db.table Blog
    blog = get_object_or_404(Blog, pk=blog_id)
    # return detail view
    return render(request, 'blog/detail.html', {'blog':blog})
