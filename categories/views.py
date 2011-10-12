# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from categories.models import Category
from django.db.models import Count
from django.template.context import RequestContext

from forms import UserForm, CategoryForm

def frontend(request):
	# cats = Category.objects.all()
	uform = UserForm(request.POST or None)
	cform = CategoryForm(request.POST or None)
	if uform.is_valid() and cform.is_valid():
		user_obj = uform.save()
		cform.save(user_obj)
		return redirect('http://inmobi.com')
	# return render_to_response('notification.html',locals(),RequestContext('request'))
	return render_to_response('notification.html',
							locals()
							)
