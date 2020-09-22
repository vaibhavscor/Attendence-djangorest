from django.contrib import admin

# Register your models here.
from .models import Users_custom, Attendence


admin.site.register(Users_custom)
admin.site.register(Attendence)
