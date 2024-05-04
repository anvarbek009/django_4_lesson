from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'
    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    descriptions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='products/',blank=True, null=True)
    
    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name