from django.contrib import admin

from recipe_app.models import Tourism, User, loginTable

# Register your models here.

admin.site.register(User)
admin.site.register(loginTable)
admin.site.register(Tourism)