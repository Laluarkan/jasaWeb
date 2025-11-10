from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'get_user_email', 'status', 'created_at')
    list_filter = ('status',)
    list_editable = ('status',)

    search_fields = ('project_name', 'user__username', 'user__email')
    autocomplete_fields = ('user',) # <-- DENGAN BARIS INI

    # Fungsi untuk menampilkan email di daftar (biarkan)
    @admin.display(description='User (Email)', ordering='user__email')
    def get_user_email(self, obj):
        return obj.user.email