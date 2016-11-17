from django.contrib import admin
from app_crm.models import Asset, Company, Note, Tag, Task



class AssetAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number', 'email')

admin.site.register(Asset, AssetAdmin)


admin.site.register(Company)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_creator', 'note_is_about')

admin.site.register(Note, NoteAdmin)


admin.site.register(Tag)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('creator', 'assigned_to', 'task_is_about')

admin.site.register(Task, TaskAdmin)
