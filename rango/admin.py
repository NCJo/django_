from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# This class will customize the admin interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


# Register your models here.

# Update the registration to include this customized interface
admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)