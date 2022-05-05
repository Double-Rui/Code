import datetime
import json

import MySQLdb
from django.core.cache import cache
from .models import Messages, Messageslist, Groupmembers


def getMessages(sqlstr):
    conn = MySQLdb.connect(host='localhost',user='root',password='123456',database='gochat',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    try:
        # 执行SQL语句
        # print(sqlstr)
        cursor.execute(sqlstr)
        result =cursor.fetchall()
        return result
    except Exception as e:
        conn.rollback()
    cursor.close()
    conn.close()

def get_Messages_record(UserID,FriendID,Messagestype):
    messages = cache.get("cache_Messages_record")
    if messages is None:
        print("messages is None")
        messages=Messages.objects.filter(SendTime__gte=datetime.datetime.now()-datetime.timedelta(days=30))
        cache.set("cache_Messages_record",messages)

    result = ''
    if(Messagestype=='friend'):
        messages1 = messages.filter(FromUserID = UserID, ToUserID = FriendID,MessagesType = 'friend')
        messages2 = messages.filter(FromUserID = FriendID, ToUserID = UserID,MessagesType = 'friend')
        a=messages1 | messages2
        b=a.order_by('SendTime').values("PostMessages","SendTime","MessagesType","FromUserID","ToUserID")
        # result.append({"SessionID": FriendID,"Session": list(b)})
        result={"SessionID": FriendID,"Session": list(b)}
    elif(Messagestype=='group'):
        groupmembers=Groupmembers.objects.get(userid=UserID,groupid=FriendID)
        sqlstr="SELECT home_messages.PostMessages, home_messages.SendTime, `user`.UserName,home_messages.FromUserID,home_messages.ToUserID,home_messages.MessagesType,`user`.HeadPortrait " \
               "FROM home_messages " \
               "INNER JOIN `user` ON home_messages.FromUserID = `user`.LoginID " \
               "WHERE home_messages.ToUserID = "+FriendID+" AND home_messages.MessagesType = 'group' AND home_messages.SendTime >= '"+groupmembers.jointime+"'"
        a=getMessages(sqlstr)
        # messages1 = messages.filter(ToUserID=FriendID, MessagesType = 'group')
        # a = messages1.order_by('SendTime').values("PostMessages", "SendTime", "MessagesType", "FromUserID", "ToUserID")
        result = {"SessionID": FriendID, "Session": list(a)}
    return result