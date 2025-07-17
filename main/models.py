from django.db import models

class Cloth(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothes/')
    size = models.CharField(max_length=2, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large')])

    def __str__(self):
        return self.name
