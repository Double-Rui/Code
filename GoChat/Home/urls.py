from django.urls import path
# from .views import
from .views import *

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    # path('GoChat/', Recent_chat),
    # path('Home/Friends_list/', Friends_list),
    # path('Home/Find_Friends/', Find_Friends),
    # path('Home/Chat_panel', Chat_panel),
    path('EditSign', EditSign),
    path('EditUserName', EditUserName),
    path('getFriendInfo', getFriendInfo),
    path('getGroupInfo', getGroupInfo),
    path('ToChat',ToChat),
    path('EditUserInfo',EditUserInfo),
    path('Findfriends',Find_friends),
    path('Findgroups', Find_groups),
    path('EditAvatar',EditAvatar),
    path('getFriendGroups',getFriendGroups),
    path('getAddFriend_applylist',getAddFriend_applylist),
    path('getAddGroup_applylist', getAddGroup_applylist),
    path('verificat_isfriend',verificat_isfriend),
    path('Processing_requests',Processing_requests),
    path('ChangePassword',ChangePassword),
    path('NewSession',NewSession),
    path('DeleteSession',DeleteSession),
    path('DeleteFriend', DeleteFriend),
    path('EditFriendname', EditFriendname),
    path('EditFriendGroup', EditFriendGroup),
    path('getFriendGroup', getFriendGroup),
    path('MoveFriendGroup', MoveFriendGroup),
    path('AddFriendGroup', AddFriendGroup),
    path('DeleteFriendGroup', DeleteFriendGroup),
    path('EditFriendGroupname', EditFriendGroupname),
    path('RefreshRecentmessage', RefreshRecentmessage),
    path('EditHeaderstyle', EditHeaderstyle),
    path('getGroupslist', getGroupslist),
    path('EditGroupname', EditGroupname),
    path('EditGroupUserremarks', EditGroupUserremarks),
    path('Editgroupverification', Editgroupverification),
    path('Disbandgroup', Disbandgroup),
    path('Exitgroup', Exitgroup),
    path('SetupAdmin', SetupAdmin),
    path('RemoveMembers', RemoveMembers),
    path('EditProfile', EditProfile),
]