from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class InventoryRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} - {self.date}"