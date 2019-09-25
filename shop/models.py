import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    # Example field up to be changed, remember to migrate database after changing models
    account_name = models.CharField(max_length=200)


class Driver(models.Model):
    # Example field up to be changed, remember to migrate database after changing models
    driver_name = models.CharField(max_length=200)


class Shopper(models.Model):
    # Example field up to be changed, remember to migrate database after changing models
    shopper_name = models.CharField(max_length=200)


class Item(models.Model):
    # Example field up to be changed, remember to migrate database after changing models
    item_name = models.CharField(max_length=200)


class Store(models.Model):
    # Example field up to be changed, remember to migrate database after changing models
    store_name = models.CharField(max_length=200)
