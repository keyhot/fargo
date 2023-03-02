from django.contrib import admin
from .models import Job, Member


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "wage",)


class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")


admin.site.register(Job, JobAdmin)
admin.site.register(Member, MemberAdmin)