from django.db import models
from django.urls import reverse

class product(models.Model):
    name = models.CharField(max_length=150)
    Price = models.DecimalField(max_digits=15,decimal_places=3)
    Description = models.TextField(max_length=150)
    
    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
