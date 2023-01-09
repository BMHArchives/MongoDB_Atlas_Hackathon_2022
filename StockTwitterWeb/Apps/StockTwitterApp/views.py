from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Stock

class UserStocksListView(generic.ListView):
      model = Stock
      context_stock = 'user_stocks_list'
      queryset = Stock.objects.all()
      template_name = 'users_stock_list.html'
      
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
