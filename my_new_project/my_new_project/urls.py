"""my_new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from university import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.main_page),
    url(r'^home/',views.home_page),
    url(r'^contact',views.contact_page),
    url(r'^courses/',views.courses_page),
    url(r'^feedback/',views.feedback_page),
    url(r'^ourteam/',views.ourteam_page),
    url(r'^gallery',views.gallery_page)
]
