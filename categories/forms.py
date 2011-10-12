from models import Category, UserInfo, UserCategory
from django import forms

class UserForm(forms.ModelForm):

	class Meta:
		model = UserInfo


class CategoryForm(forms.Form):
	def __init__(self,*args,**kwargs):
		super(CategoryForm,self).__init__(*args,**kwargs)
		cat = Category.objects.all()
		for el in cat:
			self.fields[el.name] = forms.BooleanField(required=False)
		
	def save(self,user_obj):
		to_save = [Category.objects.get(name=el) for el in self.cleaned_data if self.cleaned_data[el]]
		for el in to_save:
			UserCategory.objects.create(user=user_obj,
						category=el)
			
