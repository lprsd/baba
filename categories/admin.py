from django.contrib import admin
from models import Category, UserInfo, UserCategory

admin.site.register(Category)

class CategoryInline(admin.TabularInline):
	model = UserCategory

class UserInfoAdmin(admin.ModelAdmin):
	inlines = [CategoryInline,]

admin.site.register(UserInfo,UserInfoAdmin)
