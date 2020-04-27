from django.contrib import admin
from blog.models import Post, Category, Tag, AboutMe, Banner, ChickenSoup


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'avatar', 'excerpt', 'category', 'tags']
    list_display_links = ['title']
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    list_display_links = ['description']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    list_display_links = ['description']


class ChickenSoupAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    list_display_links = ['description']


# 注册数据表后，后台可以添加
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(ChickenSoup, ChickenSoupAdmin)

# 修改头部信息和标题信
admin.site.site_header = '博客后台管理'
admin.site.site_title = '博客管理'
