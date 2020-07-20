# Django Core
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Owner
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email',)
    fieldsets = (
            (None, {'fields': (
                'email',
                'password',
                'first_name',
                'last_name',
                'is_active',
                'is_staff',
                'is_student',
                'is_teacher'
            )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # overrides get_fieldsets to use this attribute when creating a user.
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(User)
class UserAdmon(UserAdmin):
    list_display = ('id', 'username', 'is_student', 'is_teacher')
    