from django.contrib import admin

from .models import Room,Topic,Message,User

class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email",]
    list_display_links = ["name", "email",]
    empty_value_display = "unknown"
    search_fields = ["name", "email", "username"]
    list_filter = ["is_superuser","is_staff","is_active"]


class RoomAdmin(admin.ModelAdmin):
    list_display = ("host", "topic", "name")
    list_display_links = ("host", "topic", "name")
    ordering = ["created"]
    search_fields = ("name", "description")
    list_filter = ("created","updated")


class TopicAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "room", "body")
    list_display_links = ("user", "room")
    ordering = ["created"]
    search_fields = ["body"]
    list_filter = ("created","updated")


admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)
