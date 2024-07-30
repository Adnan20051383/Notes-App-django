from django.contrib import admin

from notes.models import Note


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'datetime')


admin.site.register(Note, NotesAdmin)


