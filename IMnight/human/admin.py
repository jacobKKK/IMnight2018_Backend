from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from human.models import Profile, Relationship
from human.chat.models import Message


class RelationshipInLine(admin.StackedInline):
    model = Relationship
    extra = 0
    exclude = ['created']


class ClientInLine(RelationshipInLine):
    fk_name = 'client'


class PerformerInLine(RelationshipInLine):
    fk_name = 'performer'


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInLine, ClientInLine, PerformerInLine,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('label', 'client', 'performer')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'handle', 'message', 'timestamp')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Message, MessageAdmin)
