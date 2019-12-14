from django.contrib import admin
from .models import Supervisor, Employee, Machine, User, Downtime
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class MachineList(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name')
    ordering = ['id']


admin.site.register(Machine)
admin.site.register(Downtime)
admin.site.register(User, UserAdmin)
admin.site.register(Supervisor)
admin.site.register(Employee)

