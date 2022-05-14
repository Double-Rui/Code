from django.urls import path
from .views import *

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('Register/', Register),
    path('Login', Login),
    path('Logout', Logout),
    path('users/dashboard/', dashboard),
    path('ForgotPassword', ForgotPassword),
    path('Verifyaccount', Verifyaccount),
    path('Verifysecurity', Verifysecurity),
    path('ResetPassword', ResetPassword),
    path('SecurityCenter', SecurityCenter),
    path('EditSecretprotec',EditSecretprotec)
]