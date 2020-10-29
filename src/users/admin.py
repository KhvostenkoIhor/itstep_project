from django.contrib import admin

from .models import User, Role, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("last_login", "date_joined")


@admin.register(Profile)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass



















