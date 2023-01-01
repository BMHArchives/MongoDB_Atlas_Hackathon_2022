from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# StockTwitterApp/AppUser
# class AppUser(AbstractUser):
#       pass

#       def __str__(self):
#           return self.username
    
class Stock(models.Model):
      
      """Model representing a user's selected stock

      Args:
            models (_type_): _description_
      """
      id = models.UUIDField(primary_key=True, default=uuid.uuid4)
      name = models.TextField('Stock Name', max_length=1000, null=False)
      symbol = models.TextField('Ticker Symbol', max_length=100, null=False)
      tags = models.TextField('Search Tags', max_length=1000, help_text="Enter additional keywords to use in the search ('#XBox', 'IOS')")
      active=models.BooleanField('Activate or Deactivate', default=True, help_text="Check to activate the stock or uncheck to deactivate the stock.")
      
      #user=models.ForeignKey(User, on_delete=models.CASCADE)
      user = models.ForeignKey(User,  on_delete=models.CASCADE)
      def __str__(self):
          return f'{self.name} - {self.symbol}'
      
      class Meta:
            ordering=['-name']
                   
      def get_absolute_url(self):
          """Returns the URL to access a detail record for this stock."""
          return reverse('stock-detail', args=[str(self.id)])
      

