from turtle import title
from django.contrib import admin
from .models import todoItem

# Register your models here.
class todoListAdminConfig(admin.ModelAdmin):
    model = todoItem
    search_fields = ('id', 'title')
    list_filter = ('isFinished',)
    ordering = ('-modified',)
    list_display = ('title', 'ownerUsername', 'isFinished')
    # fieldsets = (
    #     (None, {'fields': ('id', 'title')})
    # )
    # fields: Optional[_FieldGroups]

admin.site.register(todoItem, todoListAdminConfig)