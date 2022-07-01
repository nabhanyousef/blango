from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post
admin.site.register(Tag)
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    prepopulated_fields = {"slug": ("published_at",)}
    prepopulated_fields = {"Tag": ("Post",)}
    
        