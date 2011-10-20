from models import Category, UserInfo, UserCategory
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):

	def clean_email_id(self):
		try:
			ui = UserInfo.objects.get(email_id=self.cleaned_data['email_id'])
			ui.send_edit_link()
			raise forms.ValidationError('This email is already registered. Check email for a link to edit preferences.')
		except UserInfo.DoesNotExist:
			return self.cleaned_data['email_id']

	class Meta:
		model = UserInfo
		exclude = ['user','userhash']

class UserDispForm(forms.ModelForm):

	class Meta:
		model = UserInfo
		exclude = ['user','userhash','email_id']

class EmailForm(forms.Form):

	email_id = forms.EmailField()

	def clean_email_id(self):
		try:
			ui = UserInfo.objects.get(email_id=self.cleaned_data['email_id'])
			ui.send_edit_link()
			return self.cleaned_data['email_id']
		except UserInfo.DoesNotExist:
			raise forms.ValidationError('This email is not registered')



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

