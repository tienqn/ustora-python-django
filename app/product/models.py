from django.db import models
from django.contrib.auth.models import User

class ProductCategory(models.Model):
    title = models.TextField(max_length=100)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=255, default='')
    origil_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_count = models.IntegerField(default=0)
    added_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    
    def  __str__(self):
        return self.title

class ProductTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title

class ViewedProduct(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    view_time = models.DateTimeField()
    
    def  __str__(self):
        return self.product_id.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='asset/images/products')
    is_main_image = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.title}"