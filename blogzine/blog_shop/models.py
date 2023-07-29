from django.db import models

class Cart(models.Model):
    products = models.ManyToManyField('Product', through='CartItem', related_name='carts')

    def __str__(self):
        return f'Cart {self.pk}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cart} - {self.product} ({self.quantity})'
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    cart = models.ManyToManyField(Cart, through='CartItem', blank=True)

    def __str__(self):
        return self.name


