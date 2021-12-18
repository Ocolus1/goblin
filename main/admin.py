from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

from main.models import Player_detail, Level, User

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class PlayerInline(admin.StackedInline):
#     model = Player
#     can_delete = False
#     verbose_name_plural = 'player'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (PlayerInline,)

class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            "fields": ( "username", "address", "password")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_superuser", "is_staff")
        })
    )
    fieldsets = (
        (None, {
            "fields": ("username", "address", "password")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_superuser", "is_staff")
        })
    )
    list_display = ["username", "address"]
    search_fields = ("address", "username")
    ordering = ("address",)

# Re-register UserAdmin
# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Player_detail)
admin.site.register(Level)