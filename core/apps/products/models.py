from django.db import models
from apps.accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name_plural = "Categories"

# Create your models here.
class Product(models.Model):
    # related_name="products" makes it easier to access products added by a specific user using user.products.all()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['-created_at']),
        ]