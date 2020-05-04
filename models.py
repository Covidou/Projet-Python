#!/bin/python3
# -*- coding: utf-8 -*-
# Authors @Flexiboy

from django.db import models

class Product(models.Model):
	productId = models.CharField(max_length=8, primary_key=True)
	nom = models.CharField(max_length=20)

class User(models.Model):
	userId = models.CharField(max_length=8, primary_key=True)
	email = models.CharField(max_length=30, default='name@email.com')
	phone = models.CharField(max_length=10, default='0000000000')
	numberOfPeople = models.IntegerField(default=1)
	address = models.CharField(max_length=50)
	password = models.CharField(max_length=50, default='password')
	cityId = models.ForeignKey(City, on_delete=models.DO_NOTHING)

class City(models.Model):
	cityId = models.CharField(max_length=8, primary_key=True)
	postalCode = models.CharField(max_length=5, default='00000')
	name = models.CharField(max_length=20)

class District(models.Model):
	districtId = models.CharField(max_length=8, primary_key=True)
	name = models.CharField(max_length=20)
	cityId = models.ForeignKey(City, on_delete=models.DO_NOTHING)

class Order(models.Model):
	orderId = models.CharField(max_length=8, primary_key=True)
	userId = models.ManyToManyField(User)
	cityId = models.ManyToManyField(City)
	orderDate = models.DateTimeField(auto_now=False, auto_now_add=True)
