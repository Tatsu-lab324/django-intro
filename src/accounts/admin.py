from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Profile
from .forms import CustomAdminChangeForm

class UserAdmin(BaseUserAdmin):
    form = CustomAdminChangeForm

    list_display = (
        "email",
        "active",
        "staff",
        "admin",
    )

    list_filter = (
        "admin",
        "active",
    )
    ordering = ("email",)
    filter_horizontal = ()

    search_fields = ("email",)

    add_fieldsets = (
        (None,{
            "classes":("wide",),
            "fields":("email","password1","password2")
            }
        ),
    )

    fieldsets = (
        (None,{"fields":("email","password",)}),
        ("権限",{"fields":("staff","admin",)}),
        ('プロフィール', {'fields': (
            'username',
            'department',
            'phone_number',
            'gender',
            'birthday',
        )}),
    )

admin.site.register(User,UserAdmin)
admin.site.register(Profile)
