from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from django.contrib.auth.admin import UserAdmin

from .models import Stock
#from .forms import AppUserCreationForm, AppUserChangeForm
# Register your models here.
#admin.site.register(Stock)

# Define admin class

class StockAdmin(admin.ModelAdmin):
      list_display = ('name', 'symbol', 'tags', 'user')
      list_filter = ('name', 'symbol', 'user')
      fields = ['name', 'symbol', 'tags', 'user']
admin.site.register(Stock, StockAdmin)
#class AppUserAdmin(UserAdmin):
#      add_form = AppUserCreationForm
#      form = AppUserChangeForm
#      model= AppUser
#      list_display = ("email", "username")
#admin.site.register(AppUser, AppUserAdmin)        
>>>>>>> a810867 (Updated .gitignore file.)
