from django.contrib import admin
from notice.models import Person, Category, School, Notice


# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "dateOfBirth") # change korte hobe eituk

    def active(self, obj):
        return obj.is_active == 1
    
    active.boolean = True

    
    def has_delete_permission(self, request, obj = None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Person, PersonAdmin)
admin.site.register(Category)
admin.site.register(School)
admin.site.register(Notice)

# Customization

admin.site.site_header = "NoticeBoard Admin Panel"
admin.site.site_title = "Admin Portal Sourav"
admin.site.index_title = "Hello and welcome to"

