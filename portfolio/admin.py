from django.contrib import admin
from .models import Project, ProjectImage, ContactMessage


class ProjectImageInline(admin.TabularInline):
    """Shows image upload fields inside the Project admin page"""
    model = ProjectImage
    extra = 3  # Shows 3 empty image fields by default
    fields = ['image', 'caption', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'client', 'created_at']
    list_filter = ['category']
    search_fields = ['title', 'description', 'client']
    inlines = [ProjectImageInline]  # Adds image upload section


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order']
    list_filter = ['project']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']