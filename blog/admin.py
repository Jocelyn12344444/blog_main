from django.contrib import admin
from .models import post, category, comment


admin.site.register(post)
admin.site.register(category)
admin.site.register(comment)
