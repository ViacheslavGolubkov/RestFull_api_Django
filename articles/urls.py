from django.contrib import admin
from django.urls import path, include
from articles.views import *
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'posts', ArticleViewSet, basename='posts')

app_name = 'article'
urlpatterns = [
    path('', include(routers.urls)), #127.0.0.1/api/v1/article
    path('auth/', include('djoser.urls'))
]