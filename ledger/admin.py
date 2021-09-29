from django.contrib import admin
from .models import User, Wallet, Category, Transaction

# Register your models here.
admin.site.register(User)
admin.site.register(Wallet)
admin.site.register(Category)
admin.site.register(Transaction)