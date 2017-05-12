"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    
    /
    /login/
    /signup/
    /question/<123>/ 
    /ask/
    /popular/
    /new/
    
    
    (?P<question_id>[0-9]+)/
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.question_all, name='question_all'),
    url(r'^popular/', views.question_popular_all, name='question_popular_all'),
    url(r'^question/(?P<question_id>[0-9]+)/', views.question_details, name='question_details'),
]