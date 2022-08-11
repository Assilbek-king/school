"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path as url
from django.views.static import serve
from school import settings
from siteapp.views import indexHandler, aboutHandler, teacherHandler, galleryHandler, contactHandler, \
    postItemHandler, postHandler, gosHandler
from main.views import classHandler, classItemHandler, studentItemHandler, \
    studentHandler, prepodHandler, prepodItemHandler, vhodHandler, exitHandler, \
    mainHandler, lessonHandler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexHandler),
    path('about', aboutHandler),
    path('teacher', teacherHandler),
    path('gallery', galleryHandler),
    path('contact', contactHandler),
    path('post', postHandler),
    path('gos', gosHandler),
    path('post/<int:post_id>', postItemHandler),
    path('<int:post_id>', postItemHandler),

    # ****************************
    path('main', mainHandler),
    path('login', vhodHandler),
    path('logout', exitHandler),
    path('main/class', classHandler),
    path('main/class/<int:sinf_id>', classItemHandler),
    path('main/student', studentHandler),
    path('main/student/<int:student_id>', studentItemHandler),
    path('main/prepod', prepodHandler),
    path('main/prepod/<int:prepod_id>', prepodItemHandler),
    path('main/lesson', lessonHandler),


    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]
