from django.db import models

# Create your models here.

class Categories(models.Model):
    CategoriesID = models.IntegerField(primary_key=True)
    CategoriesName = models.CharField(max_length=50)
    CategoriesDescription = models.TextField(max_length=100)
    class Meta:
        managed = True
        db_table = 'categories'

    def __str__(self):
        return self.CategoriesName
class Products(models.Model):
    ProductsID = models.IntegerField(primary_key=True)
    ProductsName = models.CharField(max_length=50)
    ProductsDescription = models.TextField(max_length=100)
    ProductsPrice = models.DecimalField(decimal_places=3, max_digits=10)
    ProductsNumber = models.IntegerField(default=0)
    ProductsImage = models.ImageField(null=True, blank=True, upload_to="None")
    CategoriesID = models.ForeignKey(Categories, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'products'

    def __str__(self):
        return self.ProductsName