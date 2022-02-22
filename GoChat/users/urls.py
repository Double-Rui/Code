from django.urls import path
from .views import Register,Login,Logout,dashboard

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('Register/', Register),
    path('Login', Login),
    path('Logout', Logout),
    path('users/dashboard/', dashboard, name='dashboard'),
]