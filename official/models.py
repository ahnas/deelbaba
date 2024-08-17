from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.name)
    

class Product(models.Model):
    productcategory = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    price = models.BigIntegerField()
    photo = models.ImageField(upload_to='images/products')

    def __str__(self):
        return str(self.name)
