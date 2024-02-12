from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Document, Category

admin.site.register(Document,SimpleHistoryAdmin)
admin.site.register(Category,SimpleHistoryAdmin)
