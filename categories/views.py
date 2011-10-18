# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.db.models import Count
from django.template.context import RequestContext

from forms import UserForm, CategoryForm, UserCreationForm
from categories.models import UserInfo, Category

from django.contrib.auth import authenticate, login

def frontend(request):
	if request.user.is_authenticated():
		return frontend_user(request)
	else:
		usform = UserCreationForm(request.POST or None)
		uform = UserForm(request.POST or None)
		cform = CategoryForm(request.POST or None)
	if request.method=='POST' and usform.is_valid() and uform.is_valid() and cform.is_valid():
		signed_up_user = usform.save()
		user = authenticate(username=usform.cleaned_data['username'],
		             password=usform.cleaned_data['password1'])
		login(request,user)
		user_obj = uform.save(commit=False)
		user_obj.user = signed_up_user
		user_obj.save()
		cform.save(user_obj)
		return redirect('http://inmobi.com')
	return render_to_response('notification.html',
	                          locals(),
	                          RequestContext(request))


def frontend_user(request):
	userinfo = UserInfo.objects.get(user=request.user)
	uform = UserForm(instance=userinfo)
	cform = CategoryForm(user_instance=userinfo)
	if request.method=='POST' and uform.is_valid() and cform.is_valid():
		user_obj = uform.save()
		cform.save(user_obj)
		return redirect("http://google.com")
	return render_to_response('notification.html',
	                          locals(),
	                          RequestContext(request))
