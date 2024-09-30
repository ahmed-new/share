from django.contrib import admin
from .models import Post , Category , Profile , Comment


class Postsadmin(admin.ModelAdmin):
    list_display=("author","title","category")
    search_fields=["id"]
    list_filter=("id","date")

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'body')
                   

admin.site.register(Post ,Postsadmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment , CommentAdmin)




# Register your models here.
