from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from users.models import User

class AuthMD(MiddlewareMixin):
    white_list = ['/','/Login', '/Register/' ]  # 白名单
    black_list = ['Home/Recent_chat/','Home/Friends_list/','Home/Find_Friends/', ]  # 黑名单
    def process_request(self, request):
        print(request.path)
        if request.path in self.white_list:
            return None
        LoginID=request.COOKIES.get('LoginID')
        if not LoginID:
            return HttpResponseRedirect('/Login')
        users=User.objects.filter(loginid=LoginID)
        if not users:
            return HttpResponseRedirect('/Login')
        request.user=users[0]
