from models import Category, UserInfo, UserCategory
from django import forms
from django.contrib.auth.forms import UserCreationForm
from IPython import embed


class UserForm(forms.ModelForm):

	class Meta:
		model = UserInfo
		exclude = ['user']

class CategoryForm(forms.Form):
	def __init__(self,user_instance=None,*args,**kwargs):
		super(CategoryForm,self).__init__(*args,**kwargs)
		cat = Category.objects.all()
		for el in cat:
			self.fields[el.name] = forms.BooleanField(required=False)
		if user_instance:
			selected_cats = UserCategory.objects.filter(user=user_instance).values_list('category__name',flat=True)
			for el in selected_cats:
				self.initial[el] = True

	def save(self,user_obj):
		# embed()
		to_add = [el for el in self.cleaned_data if self.cleaned_data[el]]
		# to_save = [Category.objects.get(name=el) for el in self.cleaned_data if self.cleaned_data[el]]
		to_delete = [el for el in self.changed_data if not el in to_add]
		# embed()
		for el in to_add:
			UserCategory.objects.get_or_create(user=user_obj,
			                            	category=Category.objects.get(name=el))
		for el in to_delete:
			UserCategory.objects.filter(user=user_obj,category__name=el).delete()

