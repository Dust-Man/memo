from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'emergency_phone']  # Mostrar estos campos en la lista del admin
    search_fields = ['user__username', 'full_name', 'emergency_phone']  # Campos de búsqueda

admin.site.register(Profile, ProfileAdmin)
