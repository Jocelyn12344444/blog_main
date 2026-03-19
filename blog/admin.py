from django.contrib import admin
from .models import Post, category, comment


admin.site.register(Post)
admin.site.register(category)
admin.site.register(comment)
