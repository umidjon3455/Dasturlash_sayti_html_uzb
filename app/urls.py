from django.contrib import admin
from django.urls import path, include
from .views import news_list, news_detail, home_page, uzb_page

urlpatterns = [
    path('', home_page, name='home'),
    path('uzbekiston', uzb_page, name='uzb'),
    path("news/<int:id>/", news_detail, name='news_detail_page')
]


