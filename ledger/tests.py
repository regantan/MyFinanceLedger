import os
import pathlib
import unittest

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client, TestCase, LiveServerTestCase
from selenium import webdriver

from .models import User, Wallet, Category, Transaction

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Login user: djangotest
def login_method(self):
    driver.get(f"{self.live_server_url}/login")
    username_input = driver.find_element_by_name("username")
    password_input = driver.find_element_by_name("password")
    username_input.send_keys('djangotest')
    password_input.send_keys('djangotest')
    username_input.submit()
        
# Sets up web driver using Google chrome
driver = webdriver.Chrome()

# Create your tests here.
class LedgerTesting(TestCase):
    pass
        
class WebpageTesting(StaticLiveServerTestCase):
    
    
    def setUp(self):
        username = "djangotest"
        email = "djangotest@test.com"
        password = "djangotest"
        user = User.objects.create_user(username, email, password)
        user.save()
        
    def test_register(self):
            
        """Tests user register page"""
        driver.get(f"{self.live_server_url}/register")
        username_input = driver.find_element_by_name("username")
        username_input.send_keys('test')
        email_input = driver.find_element_by_name("email")
        email_input.send_keys('test@test.com')
        password_input = driver.find_element_by_name("password")
        password_input.send_keys('test')
        confirmation_input = driver.find_element_by_name("confirmation")
        confirmation_input.send_keys('test')
        username_input.submit()
        
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test')
        
        """Tests wallets and categories made"""
        wallets = Wallet.objects.filter(owner=user)
        self.assertEqual(wallets.count(), 1)
        
        categories = Category.objects.filter(user=user)
        self.assertEqual(categories.count(), 5)
    
    def test_login(self):
        """Tests user login page"""
        driver.get(f"{self.live_server_url}/login")
        username_input = driver.find_element_by_name("username")
        password_input = driver.find_element_by_name("password")
        username_input.send_keys('djangotest')
        password_input.send_keys('djangotest')
        username_input.submit()
        self.assertEqual(driver.title, 'MyFinanceLedger: djangotest')
        
    def test_new_categories(self):
        """Tests user adding new category name"""
        login_method(self)
        driver.get(f"{self.live_server_url}/categories")
        driver.find_element_by_class_name("new_category_button").click()
        category_name = driver.find_element_by_name("category_name")
        category_name.send_keys("TEST")
        category_name.submit()
        
        user = User.objects.get(username='djangotest')
        category = Category.objects.get(user=user)
        self.assertEqual(category.category_name, 'TEST')
        
        
if __name__ == "__main__":
    unittest.main()