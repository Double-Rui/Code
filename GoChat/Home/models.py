from django.db import models

class Addfriends(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True) #主键ID 主键
    applicantid = models.IntegerField(db_column='ApplicantID',primary_key=True) #ID 外键
    userid = models.IntegerField(db_column='UserID') #申请者ID 外键
    objectid = models.IntegerField(db_column='ObjectID') #添加对象的ID 外键
    friendsGroupid = models.IntegerField(db_column='FriendsGroupID') #分组id
    addway = models.CharField(db_column='Addway', max_length=50, blank=True, null=True) #添加方式 Null（30）
    remarksname = models.CharField(db_column='Remarksname', max_length=10, blank=True, null=True)  # 备注    外键
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True) #备注    外键
    sendtime = models.CharField(db_column='Sendtime', max_length=50, blank=True, null=True) #发送时间    外键
    responsetime = models.CharField(db_column='Responsetime', max_length=50, blank=True, null=True) #回应时间    外键
    rep_results = models.IntegerField(db_column='Rep_results') #回应结果

class AddGroups(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True) #主键ID 主键
    applicantid = models.IntegerField(db_column='ApplicantID',primary_key=True) #申请者的ID 外键
    userid = models.IntegerField(db_column='UserID')  # 申请者ID 外键
    objectid = models.IntegerField(db_column='ObjectID') #添加对象的ID 外键
    addway = models.CharField(db_column='Addway', max_length=50, blank=True, null=True) #添加方式 Null（30）
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True) #备注    外键
    sendtime = models.CharField(db_column='Sendtime', max_length=50, blank=True, null=True) #发送时间    外键
    responsetime = models.CharField(db_column='Responsetime', max_length=50, blank=True, null=True) #回应时间    外键
    rep_results = models.IntegerField(db_column='Rep_results') #回应结果
    processorid = models.IntegerField(db_column='ProcessorID',default=1)  # 处理者ID 外键

class Friends(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True) #主键ID 主键
    relationid=models.IntegerField(db_column='RelationID',primary_key=True)
    friendid = models.IntegerField(db_column='FriendID') #好友ID 外键
    userid = models.IntegerField(db_column='UserID') #用户ID 外键
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True) #备注名称
    friendtypeid = models.IntegerField(db_column='FriendTypeID') #好友类型   外键
    friendgroupsid = models.IntegerField(db_column='FriendGroupsID') #所属分组    外键

class FriendType(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True) #主键ID 主键
    typename = models.CharField(db_column='TypeName',max_length=50) #好友类型 外键

class Group(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True) #主键ID 主键
    groupid = models.IntegerField(db_column='GroupID',primary_key=True) #群号 外键
    groupname = models.CharField(db_column='GroupName', max_length=10) #群名
    groupleaderid = models.CharField(db_column='GroupleaderID', max_length=50, blank=True) #群主账号
    groupavatars = models.CharField(db_column='GroupAvatars', max_length=50, blank=True,default="Groupdefault.png") #群头像
    groupintro = models.CharField(db_column='GroupIntro', max_length=50, blank=True, null=True) #群简介
    groupverification = models.IntegerField(db_column='Groupverification',default=2) #加群验证

class Groupmembers(models.Model):
    applicantid = models.IntegerField(db_column='ApplicantID', primary_key=True)  # 关系id 外键
    userid = models.IntegerField(db_column='UserID') #用户ID 外键
    groupid = models.IntegerField(db_column='GroupID')  # 群号 外键
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # 备注名称
    groupname = models.CharField(db_column='GroupName', max_length=50, blank=True, null=True)  # 备注名称
    role = models.CharField(db_column='Role', max_length=50, blank=True, null=False)  # 角色
    jointime = models.CharField(db_column='Jointime', max_length=50, blank=True, null=False)

class Messages(models.Model):
    Messagesid = models.IntegerField(db_column='MessagesID', primary_key=True) #主键ID 主键
    PostMessages = models.CharField(db_column='PostMessages',max_length=500, blank=True, null=True) #消息内容
    status = models.IntegerField(db_column='Status') #状态
    SendTime = models.CharField(db_column='SendTime', max_length=50, blank=True, null=True) #发送时间
    MessagesType = models.CharField(db_column='MessagesType', max_length=50, blank=True, null=False) #消息类型
    FromUserID = models.IntegerField(db_column='FromUserID') #发送者id
    ToUserID = models.IntegerField(db_column='ToUserID')  # 发送对象id

    # Messages_manager = models.Manager()

class Messageslist(models.Model):
    Messageslistid = models.IntegerField(db_column='MessageslistID', primary_key=True) #主键ID 主键
    userid = models.IntegerField(db_column='UserID') #用户id
    objectid = models.IntegerField(db_column='ObjectID') #对象id
    unreadnum = models.IntegerField(db_column='UnreadNum',default=0) #未读消息数量
    time = models.CharField(db_column='Time', max_length=50, blank=True, null=False)  # 时间
    messagestype = models.CharField(db_column='MessagesType', max_length=50, blank=True, null=False)  # 消息类型id
    createtime = models.CharField(db_column='CreateTime', max_length=50, blank=True, null=False)  # 创建id

class MessagesType(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True) #主键ID 主键
    typename = models.CharField(db_column='TypeName',max_length=50) #消息类型

class FriendsGroup(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True) #主键ID
    groupid = models.AutoField(db_column='GroupID', primary_key=True) #分组id 主键
    userid = models.IntegerField(db_column='UserID') #用户id
    groupname = models.CharField(db_column='GroupName',max_length=50, blank=True, null=True) #分组名
    serialnumber=models.IntegerField(db_column='SerialNumber') #分组序号
    createtime = models.CharField(db_column='CreateTime', max_length=50, blank=True, null=True)  # 创建时间

class SecurityQuestion(models.Model):
    questionid = models.AutoField(db_column='QuestionID', primary_key=True) #问题id 主键
    question = models.CharField(db_column='Question',max_length=50, blank=True, null=True) #问题