from django.contrib import admin
from .models import User

admin.site.site_header = 'GoChat管理后台'  # 设置header
admin.site.site_title = 'GoChat管理后台'   # 设置title
admin.site.index_title = 'GoChat管理后台'

class UserAdmin(admin.ModelAdmin):
    list_display = ('loginid', 'username')
    search_fields = ['loginid','username']
    # fieldsets = [
    #     ('个人信息', {'fields': ['username','password','age','sex']}),
    #     # ('Date information', {'fields': ['pub_date']}),
    # ]
    # fields=['username','age','sex','age','headportrait','phonenumber','address','bloodtype']
    # fields = ['loginid', 'username',  'headportrait']
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
admin.site.register(User,UserAdmin)
# Register your models here.
