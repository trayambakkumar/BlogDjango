from django.contrib import admin
from .models import Post

# Register your models here.

# username : trayambakkumar
# password : admin

# PostAdmin class is to modify the admin interface, the name is your class name attached with admin we
# can modify what is displayed, we can filter, also add a search interface
# The slug will pe populated on its own based on title because of prepopulated_fields


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostAdmin)


