from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    model = Post
    filter_horizontal = ('categories',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
