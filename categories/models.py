from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.core.mail import send_mail

class Category(models.Model):
	name = models.CharField(max_length=50)
	parent = models.ForeignKey('self',blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

def get_hash():
	import random
	h = str(random.random())[2:]
	return h

class UserInfo(models.Model):
	email_id = models.EmailField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	# user = models.OneToOneField(User)
	userhash = models.CharField(max_length=50)

	def save(self,*args,**kwargs):
		if not self.userhash:
			self.userhash = get_hash()
		super(UserInfo,self).save(*args,**kwargs)

	def get_edit_url(self):
		return "http://10.14.100.220:8000/notification/edit/%s/"%self.userhash

	def __unicode__(self):
		return self.email_id

	def send_edit_link(self):
		send_mail(subject='Edit notification',
				  message=self.get_edit_url(),
				  from_email='no-reply@inmobi.com',
				  recipient_list=[self.email_id,'lakshman.prasad@inmobi.com'])
		print 'Email Sent'

class UserCategory(models.Model):
	user = models.ForeignKey(UserInfo)
	category = models.ForeignKey(Category)

