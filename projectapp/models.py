from django.db import models
from django.template.defaultfilters import slugify


class Publication(models.Model):
	name=models.CharField(max_length=200)
	address=models.TextField()
	contact=models.CharField(max_length=200)
	active = models.BooleanField(default=True)
	slug=models.SlugField(blank=True,null=True)

	def save(self,*args,**kwargs):
		if self.slug is None:
			self.slug=slugify(self.name)#this will make pyblication name in slug form(ekta-books)
		super().save(*args,**kwargs)

	def __str__(self):
		return self.name

class Book(models.Model):
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=100,blank=True,null=True)
	price=models.CharField(max_length=100,blank=True,null=True)
	image=models.ImageField(upload_to='images/book',max_length=100,null=True)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	published_by=models.ForeignKey(Publication,on_delete=models.CASCADE,null=True,blank=True)#on_delete is important(mandatory) in ForeignKey so Do nothing helps to keep after removal of publictation 

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

	def __str__(self):
		return self.title

class Student(models.Model):
	name=models.CharField(max_length=100)
	address=models.TextField()

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)


	def __str__(self):
		return self.name


# Create your models here.
