from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    image=models.ImageField(upload_to='category')

    def __str__(self):
        return self.name

#OBJect RElational Mapping
class Product(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    image=models.ImageField(upload_to='product')
    price=models.DecimalField(decimal_places=2,max_digits=10)
    date_created=models.DateTimeField(auto_now_add=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

