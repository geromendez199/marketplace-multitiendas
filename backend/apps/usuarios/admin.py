from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'first_name', 'last_name', 'email', 'role', 'telefono', 'foto_perfil']
    list_filter = ['role']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefono', 'foto_perfil')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefono', 'foto_perfil')}),
    )

admin.site.register(Usuario, UsuarioAdmin)
