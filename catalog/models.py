from django.db import models
from time import time

# Create your models here.
class Computer(models.Model):
	title=models.CharField(max_length=150,db_index=True)
	slug=models.SlugField(blank=True,max_length=150,unique=True)
	cost=models.IntegerField()
	body=models.TextField(blank=True,db_index=True)
	s=models.CharField(blank=True,max_length=300)
	def save(self,*args,**kwargs):
		self.slug=self.title+str(int(time()))
		self.s='/static/catalog/images/'+self.title+'.png'
		super().save(*args,**kwargs)
	def __str__(self):
		return self.title

class Phone(models.Model):
	title=models.CharField(max_length=150,db_index=True)
	slug=models.SlugField(blank=True,max_length=150,unique=True)
	cost=models.IntegerField()
	body=models.TextField(blank=True,db_index=True)
	s=models.CharField(blank=True,max_length=300)
	def save(self,*args,**kwargs):
		self.slug=self.title+str(int(time()))
		self.s='/static/catalog/images/'+self.title+'.png'
		super().save(*args,**kwargs)
	def __str__(self):
		return self.title