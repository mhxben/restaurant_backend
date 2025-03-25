from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    status = models.CharField(max_length=20, default="free")

    def __str__(self):
        return f"Table {self.number} - {self.status}"


class Product(models.Model):
    name = models.CharField(max_length=20)
    base_price = models.FloatField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.category}"


class Customization(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (+{self.extra_price}) for {self.product.name}"


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="progress")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - Table {self.table.number} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customizations = models.ManyToManyField(Customization, blank=True)
    final_price = models.FloatField()

    def __str__(self):
        return f"{self.product.name} - Order #{self.order.id}"
