from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(blank=True, null=True)
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        
    def __str__(self):
        return str(self.image)