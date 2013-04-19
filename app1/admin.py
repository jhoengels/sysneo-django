from django.contrib import admin
from app1.models import Todo, TodoArticulo

class TodoArticuloAdmin(admin.TabularInline):
	model = TodoArticulo
	extra = 1

class TodoAdmin(admin.ModelAdmin):
	inlines = [TodoArticuloAdmin]

admin.site.register(Todo, TodoAdmin)
admin.site.register(TodoArticulo)