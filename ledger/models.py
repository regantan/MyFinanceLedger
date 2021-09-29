from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(AbstractUser):
    pass

class Wallet(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name="owner")
    
    def __str__(self):
        return f"{self.owner} has {self.name} as their wallet"

class Category(models.Model):
    category_name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="get_category_user")
    
    def __str__(self):
        return f"{self.category} by {self.user}"
    
class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('I', 'Income'),
        ('E', 'Expense'),
        ('T', 'Transfer'),
        ('B', 'Borrow'),
        ('R', 'Return'),
    )
    
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="user")
    wallet = models.ForeignKey(Wallet, on_delete=CASCADE, related_name="wallet")
    datetime = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name="get_categories")
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=64, blank=True)
    note = models.TextField()
    
    def __str__(self):
        return f"{self.user} has {self.wallet} made a {self.type} transaction at {self.datetime}, named {self.name}"
    