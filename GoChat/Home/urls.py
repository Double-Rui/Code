from django.urls import path
# from .views import
from .views import Recent_chat,Friends_list,Find_Friends,getHeadPortrait

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('Home/Recent_chat/', Recent_chat),
    path('Home/Friends_list/', Friends_list),
    path('Home/Find_Friends/', Find_Friends),
    path('Home/getHeadPortrait', getHeadPortrait),
]