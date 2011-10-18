from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=50)
	parent = models.ForeignKey('self',blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

class UserInfo(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email_id = models.EmailField()
	user = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.email_id


class UserCategory(models.Model):
	user = models.ForeignKey(UserInfo)
	category = models.ForeignKey(Category)
