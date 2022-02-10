from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('个人信息', {'fields': ['username','password','age','sex']}),
        # ('Date information', {'fields': ['pub_date']}),
    ]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
admin.site.register(User,UserAdmin)
# Register your models here.
