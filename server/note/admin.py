from django.contrib import admin
from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user', 'created_at') 
    list_filter = ('user', 'created_at')




admin.site.register(Note, NoteAdmin)

