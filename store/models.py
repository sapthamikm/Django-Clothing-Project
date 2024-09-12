from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=225)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)


    def __str__(self):
        return self.name
    

class CartItem(models.Model):

    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



        



        
