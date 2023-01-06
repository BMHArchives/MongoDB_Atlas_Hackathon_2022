from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('stocktweets', views.get_stock_tweets, name='stocktweets'),
    path('userstocks', views.get_user_stocks, name='userstocks')
]
