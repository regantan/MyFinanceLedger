from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new_transaction, name="new_transaction"),
    path("categories", views.categories, name="categories"),
    path("wallets", views.wallets, name="wallets"),
]