from django.contrib import admin
from .models import Message, Profile

class MessageAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'user', 'recipient', 'timestamp')
    list_filter = ('user', 'recipient')
    search_fields = ('recipient',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name')

admin.site.register(Message, MessageAdmin)
admin.site.register(Profile, ProfileAdmin)
