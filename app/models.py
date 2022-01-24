from django.db import models
from django.contrib.auth.models import User



class Recipe(models.Model):
    user = models.ForeignKey(User, related_name= "user_id", on_delete=models.CASCADE, default="", null=True, blank=True)
    dish = models.CharField(max_length=200, null=True, blank=True)
    ingredients = models.CharField(max_length=1000000000000000000000000, null=True, blank=True)
    description = models.CharField(max_length=1000000000000000000000000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.dish
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url