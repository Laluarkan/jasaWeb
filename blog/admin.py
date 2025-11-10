from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    # Ini akan otomatis mengisi field 'slug' saat Anda mengetik 'title'
    prepopulated_fields = {'slug': ('title',)}