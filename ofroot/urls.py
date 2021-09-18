"""ofroot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
]

# building dynamic routes
# below becomes : http://127.0.0.1:8001/media/portfolio/images/Screen_Shot_2021-06-20_at_8.52.28_AM_ttXWiMj.png
#  the image name ( 'Screen_shot...' ) comes from the uploaded image
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
