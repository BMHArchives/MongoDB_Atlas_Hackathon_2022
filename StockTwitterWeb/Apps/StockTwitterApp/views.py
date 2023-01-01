from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .models import Stock

# Create your views here.
def index(request):
    
    num_rows = Stock.objects.all().count()
    context = {
        'num_rows': num_rows
    }
    
    return render(request, 'index.html', context=context)
>>>>>>> a810867 (Updated .gitignore file.)
