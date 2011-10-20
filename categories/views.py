# Create your views here.
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from django.template.context import RequestContext
from django.contrib import messages
from forms import UserForm, UserDispForm, CategoryForm, UserCreationForm, EmailForm
from categories.models import UserInfo, Category

from django.contrib.auth import authenticate, login

def frontend_old(request):
	if request.user.is_authenticated():
		return frontend_user(request)

	usform = UserCreationForm(request.POST or None)
	uform = UserForm(request.POST or None)
	cform = CategoryForm(data=request.POST or None)
	
	if request.method=='POST' and usform.is_valid() and uform.is_valid() and cform.is_valid():
		signed_up_user = usform.save()
		newuser = authenticate(username=usform.cleaned_data['username'],
		             			password=usform.cleaned_data['password1'])
		login(request, newuser)
		user_obj = uform.save(commit=False)
		user_obj.user = signed_up_user
		user_obj.save()
		cform.save(user_obj)
		messages.success(request, 'You are signedup and logged in.')
		return redirect('.')
	return render_to_response('notification.html',
	                          locals(),
	                          RequestContext(request))

def frontend(request):
	uform = UserForm(request.POST or None)
	cform = CategoryForm(data=request.POST or None)
	
	if request.method=='POST' and uform.is_valid() and cform.is_valid():
		user_obj = uform.save(commit=False)
		user_obj.save()
		cform.save(user_obj)
		messages.success(request, 'You are signed-up for the selected notifications')
		return redirect(user_obj.get_edit_url())
	return render_to_response('notification.html',
	                          locals(),
	                          RequestContext(request))

def frontend_user(request,uhash):
	userinfo = get_object_or_404(UserInfo,userhash=uhash)
	uform = UserDispForm(instance=userinfo,data=request.POST or None)
	cform = CategoryForm(user_instance=userinfo,data=request.POST or None)
	if uform.is_valid() and uform.has_changed():
		uform.save()
		print 'Uform saved'
	if cform.is_valid() and cform.has_changed():
		cform.save(userinfo)
	if request.method=='POST':
		if (uform.has_changed() or cform.has_changed()):
			messages.success(request, 'Changes saved successfully!')
			return redirect(".")
		else:
			messages.info(request, 'No changes made!')
			return redirect(".")
	return render_to_response('notification.html',
	                          locals(),
	                          RequestContext(request))

def frontend_change(request):

	uform = EmailForm(request.POST or None)

	if uform.is_valid():
		# form.save()
		messages.info(request, 'An email has been sent, Please check')
		return redirect('.')


	return render_to_response('notification.html',
	                          locals(),
	                          RequestContext(request))
