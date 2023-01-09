
from django.urls import path, include 
from . import views
from django.contrib import admin
urlpatterns = [

    path('', views.index, name='index'),
    path('stocktweets', views.get_stock_tweets, name='stocktweets'),
    path('userstocks', views.get_user_stocks, name='userstocks'),
    path('stocks', views.UserStocksListView.as_view(), name='stocks'),
    path('accounts', include('django.contrib.auth.urls')),
]
