from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Language, Course, Category

admin.site.register(User, UserAdmin)
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Category)
