from django.contrib import admin
from .models import Post, Category, Contact


admin.site.register(Category)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ["name","email","message"]
admin.site.register(Contact, ContactusAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "date"]

admin.site.register(Post,PostAdmin)