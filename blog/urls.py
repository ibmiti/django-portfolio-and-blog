from django.urls import path
from . import views

# forces us to specify the path a bit.
    #  example : blog:detail vs. detail, or portfolio:detail
app_name = 'blog'

# list of urls
urlpatterns = [
    path( '',  views.all_blogs, name='all_blogs'),
    # pass forward whatever int ( number ) they enter
        # ex : blog/5
            # Ultimately they'll be returned the 5th blog found within the server. or the article/blog with the id of 5 or whatever number is entered into the url/path
    path( '<int:blog_id>/', views.detail, name='detail'),
]
