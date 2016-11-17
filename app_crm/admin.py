from django.contrib import admin
from app_crm.models import Asset, Company, Note, Tag, Task

admin.site.register(Asset)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_regex', 'phone_number', 'email', 'website', 'street', 'street2', 'city', 'state', 'country')

# admin.site.register(User)
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('asset', 'user')

admin.site.register(Company)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('users', 'name', 'phone_regex', 'phone_number', 'website', 'street', 'street2', 'city', 'state', 'country')

# admin.site.register(Customer)
#
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('asset', 'notes')

# admin.site.register(Orginization)
#
# class OrginizationAdmin(admin.ModelAdmin):
#     list_display = ('customers')

admin.site.register(Note)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('users')

admin.site.register(Tag)

class TagAdmin(admin.ModelAdmin):
    list_display = ('users')

admin.site.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('users')
