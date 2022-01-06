from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from .models import Post

admin.site.site_header = '後臺管理系統'
admin.site.site_title = '管理後台'


# color setting
# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     color_code = models.CharField(max_length=6)
#
#     def colored_name(self):
#         return format_html(
#             '<span style="color= : #{};">{} {}</span>',
#             self.color_code,
#             self.first_name,
#             self.last_name,
#         )
#     colored_name.allow_tags = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    list_display: 顯示欄位
    list_display_links: 哪些欄位可以點選進入內容
    search_fields: 可搜尋欄位
    list_filter: 指定欄位篩選器
    """
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    # list_filter = ('id', 'content')

