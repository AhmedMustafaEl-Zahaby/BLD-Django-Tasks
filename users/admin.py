from django.contrib import admin
from .forms import *
from .models import *
class UserAdmin(admin.ModelAdmin):
    form = UserForm

admin.site.register(User , UserAdmin)
