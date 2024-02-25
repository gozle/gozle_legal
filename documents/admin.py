from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Document, Category, Language

admin.site.register(Document,SimpleHistoryAdmin)
admin.site.register(Category,SimpleHistoryAdmin)

class LanguageAdmin(admin.ModelAdmin):
    actions = ['add_custom_language']

    def add_custom_language(self, request, queryset):
        for obj in queryset:
            Language.add_language(obj.language_code, obj.language_label)
        self.message_user(request, "New language(s) added successfully.")

admin.site.register(Language, LanguageAdmin)