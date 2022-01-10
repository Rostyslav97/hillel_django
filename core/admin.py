from django.contrib import admin
from core import models

# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass

class TabularInlineLike(admin.TabularInline):
    model=models.Like

class PostAdmin(admin.ModelAdmin):
    inlines=[TabularInlineLike]
    list_display = ("title", "user")

admin.site.register(models.Post, PostAdmin)