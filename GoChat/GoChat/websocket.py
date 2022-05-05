import json
import time
import urllib
import os
import django
import pymysql
import MySQLdb
import MySQLdb.cursors

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GoChat.settings')
django.setup()


# 发送消息结构体
def message(sender, message_type, message,sendto,sendtime):
    data = json.dumps({
        'sender': sender,
        'message_type': message_type,
        'message': message,
        'sendto':sendto,
        'sendtime':sendtime
    })
    return {
        'type': 'websocket.send',
        'text': data
    }

def SystemNotice(message):
    data = json.dumps({
        'sender': 'system',
        'message_type': 'SystemNotice',
        'message': message,
    })
    return {
        'type': 'websocket.send',
        'text': data
    }

# 发送好友申请结构体
def addFriendapplicat(sender, message_type, message,sendto):
    data = json.dumps({
        'sender': sender,
        'message_type': message_type,
        'message': message,
        'sendto':sendto
    })
    return {
        'type': 'websocket.send',
        'text': data
    }

def sqlquery(sqlstr):
    conn = pymysql.Connect(host='localhost',user='root',password='123456',database='gochat')
    cursor = conn.cursor()
    try:
        # 执行SQL语句
        print(sqlstr)
        cursor.execute(sqlstr)
        # if (cursor.rowcount > 0):
        #     print('插入数据成功')
        # else:
        #     print('插入数据失败')
        # 提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        # print(e)
        # print("sqlquery回滚")
        conn.rollback()
    cursor.close()
    conn.close()

def getgroupmembers(groupid):
    conn = MySQLdb.connect(host='localhost',user='root',password='123456',database='gochat',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sqlstr="SELECT UserID FROM home_groupmembers WHERE GroupID = '"+str(groupid)+"'"
    try:
        # 执行SQL语句
        cursor.execute(sqlstr)
        # if (cursor.rowcount > 0):
        #     print('获取群成员成功')
        # else:
        #     print('获取群成员失败')
        members =cursor.fetchall()
        return members
    except Exception as e:
        # 有异常，回滚事务
        # print(e)
        # print("getgroupmembers回滚")
        conn.rollback()
    cursor.close()
    conn.close()

def getgroupadmins(groupid):
    conn = MySQLdb.connect(host='localhost',user='root',password='123456',database='gochat',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sqlstr="SELECT UserID FROM home_groupmembers WHERE GroupID = '"+str(groupid)+"' AND Role in ('Groupleader','Administrators')"
    try:
        # 执行SQL语句
        print(sqlstr)
        cursor.execute(sqlstr)
        # if (cursor.rowcount > 0):
        #     print('获取群管理成功')
        # else:
        #     print('获取群管理失败')
        members =cursor.fetchall()
        return members
    except Exception as e:
        # 有异常，回滚事务
        # print(e)
        # print("getgroupadmins回滚")
        conn.rollback()
    cursor.close()
    conn.close()

def IsinGroup(userid,groupid):
    conn = pymysql.Connect(host='localhost', user='root', password='123456', database='gochat')
    cursor = conn.cursor()
    sqlstr="SELECT UserID FROM home_groupmembers WHERE GroupID = '"+str(groupid)+"' AND UserID = '"+str(userid)+"'"
    try:
        # 执行SQL语句
        cursor.execute(sqlstr)
        if(cursor.rowcount>0):
            return True
        else:
            return False
    except Exception as e:
        # 有异常，回滚事务
        # print(e)
        # print('IsinGroup回滚')
        conn.rollback()
    cursor.close()
    conn.close()

CONNECTIONS={}

async def websocket_application(scope,receive,send):
    while True:
        event = await receive()
        # auth = ''
        # print('[event]',event)
        # print('[scope]', scope['headers'][10])
        #收到建立Websocket连接的消息
        if event['type']=='websocket.connect':
            await send({'type':'websocket.accept'})

            #得到auth
            query_sring = scope['query_string'].decode()
            qs = urllib.parse.parse_qs(query_sring)
            auth = qs.get('auth',[''])[0]
            SqlStr = "UPDATE user SET LoginStatus = 1 WHERE LoginID = '" + auth + "'"
            sqlquery(SqlStr)
            CONNECTIONS[auth] =send

        # 收到中断Websocket连接的消息
        elif event['type']=='websocket.disconnect':
            auth = qs.get('auth', [''])[0]
            SqlStr = "UPDATE user SET LoginStatus = 0 WHERE LoginID = '"+auth+"'"
            sqlquery(SqlStr)
            break
        #其他情况，正常的websocket消息
        elif event['type'] == 'websocket.receive':
            receive_msg = json.loads(event['text'])
            # print(receive_msg)
            # message_type = receive_msg.get('message_type', 'data')
            message_type = receive_msg['message_type']

            if(message_type=='Friendmessage'):
                content = receive_msg.get('message', '')
                to_user = receive_msg.get('to_user', '')
                SqlStr = "insert into home_messages (PostMessages,Status,SendTime,MessagesType,FromUserID,ToUserID) values('" + content + "',1,'" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "','friend'," + auth + "," + to_user + ")"
                # print(SqlStr)
                sqlquery(SqlStr)
                if to_user in CONNECTIONS:
                    msg = message(auth, message_type, content,to_user,time.strftime('%H:%M:%S', time.localtime()))
                    await CONNECTIONS[to_user](msg)
                else:
                    SqlStr = "update home_messageslist set UnreadNum=UnreadNum+1 where UserID='" + auth + "' and ObjectID='" + to_user + "' and MessagesType='friend'"
                    sqlquery(SqlStr)
            elif (message_type == 'Groupmessage'):
                content = receive_msg.get('message', '')
                to_user = receive_msg.get('to_user', '')
                SqlStr = "insert into home_messages (PostMessages,Status,SendTime,MessagesType,FromUserID,ToUserID) " \
                         "values('" + content + "',1,'" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "','group'," + auth + "," + to_user + ");"
                SqlStr2 = "update home_messageslist set UnreadNum=UnreadNum+1 where UserID='"+auth+"' and ObjectID='"+to_user+"' and MessagesType='group'"
                msg = message(auth, message_type, content, to_user,time.strftime('%H:%M:%S', time.localtime()))
                # print(msg)
                members = getgroupmembers(to_user)
                sqlquery(SqlStr)
                sqlquery(SqlStr2)
                for i in members:
                    UserID=str(i['UserID'])
                    # print(UserID)
                    if UserID in CONNECTIONS:
                        # print('发送成功')
                        await CONNECTIONS[UserID](msg)
            elif (message_type == 'friendapplicat'):
                content = receive_msg.get('Remarks', '')
                Remarksname = receive_msg.get('Remarksname', '')
                FriendsGroupID = receive_msg.get('FriendsGroupID', '')
                Addway = receive_msg.get('Addway', '')
                to_user = receive_msg.get('ObjectID', '')
                SqlStr = "insert into home_addfriends (UserID,ObjectID,FriendsGroupID,Remarksname,Addway,Remarks,Sendtime,Rep_results) values(" + auth + ","+str(to_user)+","+str(FriendsGroupID)+",'"+Remarksname+"','"+Addway+"','"+content+"','" + time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime()) + "',0)"
                if to_user in CONNECTIONS:
                    sqlquery(SqlStr)
                    msg = addFriendapplicat(auth, message_type, content, to_user)
                    await CONNECTIONS[to_user](msg)
                else:
                    sqlquery(SqlStr)
            elif (message_type == 'groupapplicat'):
                content = receive_msg.get('Remarks', '')
                Addway = receive_msg.get('Addway', '')
                GroupID = receive_msg.get('ObjectID', '')
                if(IsinGroup(auth, GroupID)):
                    msg = SystemNotice('你已经是该群的成员，不能重复添加')
                    await CONNECTIONS[auth](msg)
                else:
                    SqlStr = "insert into home_addgroups (UserID,ObjectID,Addway,Remarks,Sendtime,Rep_results) values(" + auth + "," + str(
                        GroupID) + ",'" + Addway + "','" + content + "','" + time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime()) + "',0)"
                    # print(SqlStr)
                    sqlquery(SqlStr)
                    members = getgroupadmins(GroupID)
                    for i in members:
                        UserID = str(i['UserID'])
                        if UserID in CONNECTIONS:
                            msg = addFriendapplicat(auth, message_type, content, GroupID)
                            await CONNECTIONS[UserID](msg)
                        else:
                            pass
        else:
            pass
    # print('[disconnect]')