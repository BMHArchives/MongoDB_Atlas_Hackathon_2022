from django.shortcuts import render

# Create your views here.
from .models import Stock

# Create your views here.
def index(request):
    
    num_rows = Stock.objects.all().count()
    context = {
        'num_rows': num_rows
    }
    
    return render(request, 'index.html', context=context)

def get_stock_tweets(request):
    context={}
    return render(request, 'stocktweets.html', context=context)

def get_user_stocks(request):
    context={}
    return render(request, 'userstocks.html', context=context)
