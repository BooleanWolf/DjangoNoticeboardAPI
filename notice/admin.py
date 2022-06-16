from django.contrib import admin
from notice.models import Person, Category, School, Notice


# Register your models here.

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(School)
admin.site.register(Notice)