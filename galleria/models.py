from django.db import models
from django.contrib.auth.models import User

class Gallery(models.Model):
    
    name = models.CharField(max_length=50)
    date_taken = models.DateField()
    user = models.ForeignKey(User)
    
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name="images")
    image = models.ImageField(upload_to="images")