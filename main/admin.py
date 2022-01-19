from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

from main.models import Player_detail, Level, User
from main.views import Command, Tweet, Telegram, Facebook, Ethaddress, Link, Cmd, Instagram, Youtube, Reddit, Verify

class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            "fields": ("username", "address", "payload", "password")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_superuser", "is_staff")
        })
    )
    fieldsets = (
        (None, {
            "fields": ("username", "address", "payload", "password")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_superuser", "is_staff")
        })
    )
    list_display = ["username", "address", "payload", "referrals"]
    search_fields = ("address", "username")
    ordering = ("address",)

# Re-register UserAdmin
# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Player_detail)
admin.site.register(Level)
# admin.site.register(Email)
admin.site.register(Command)
admin.site.register(Tweet)
admin.site.register(Telegram)
admin.site.register(Facebook)
admin.site.register(Ethaddress)
admin.site.register(Link)
admin.site.register(Instagram)
admin.site.register(Youtube)
admin.site.register(Reddit)
admin.site.register(Cmd)
admin.site.register(Verify)