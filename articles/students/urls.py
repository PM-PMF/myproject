"""articles URL Configuration

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

#from django.urls import path
#from .views import views as students_views
#
#path('students/',students_views.MyView.as_view(template_name='login.html'), name='my-view'),
from django.urls import path
from students import views
from .views  import ArticleListView
#import re


urlpatterns = [
#path('', views.index, name='index'),
path('',views.index, name='index'),
path('articles/', ArticleListView.as_view(), name='articles'),
path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),

 ]