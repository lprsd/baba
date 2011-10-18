from models import Category, UserInfo, UserCategory
from django import forms
from django.contrib.auth.forms import UserCreationForm



class UserForm(forms.ModelForm):

	class Meta:
		model = UserInfo
		exclude = ['user']

class CategoryForm(forms.Form):
	def __init__(self,user_instance=None,*args,**kwargs):
		super(CategoryForm,self).__init__(*args,**kwargs)
		user = kwargs.get('user_instance',None)
		cat = Category.objects.all()
		for el in cat:
			self.fields[el.name] = forms.BooleanField(required=False)
		if user:
			selected_cats = UserCategory.objects.filter(user=user).values_list('category',flat=True)
			for el in selected_cats:
				self.initial[el.name] = True
		
	def save(self,user_obj):
		to_save = [Category.objects.get(name=el) for el in self.cleaned_data if self.cleaned_data[el]]
		for el in to_save:
			UserCategory.objects.create(user=user_obj,
			                            category=el)
