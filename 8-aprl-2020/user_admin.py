from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm, RegistraionForm
class CustomUserAdmin(UserAdmin):
    ordering = ('email', )
    list_display = ['email', 'is_staff', 'is_admin']

    form =  UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    filter_horizontal = ()
admin.site.register(User,CustomUserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


