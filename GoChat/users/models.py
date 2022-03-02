# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class User(models.Model):
    loginid = models.IntegerField(db_column='LoginID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    headportrait = models.CharField(db_column='HeadPortrait', max_length=50,default='0.jpg')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', blank=True, null=True, max_length=11)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bloodtype = models.CharField(db_column='BloodType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    datebirth = models.DateField(db_column='DateBirth', blank=True, null=True)  # Field name made lowercase.
    constellation = models.CharField(db_column='Constellation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    shengxiao = models.CharField(db_column='ShengXiao', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='Sign', max_length=100, blank=True, null=True,default='')  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=50, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addtimeid = models.CharField(db_column='AddtimeID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __int__(self):
        return self.loginid

class UserInfo():
    id =""
    username = ""
    sex = ""
    age = ""
    headportrait = ""
    phonenumber = ""
    address = ""
    bloodtype = ""
    datebirth = ""
    constellation = ""
    shengxiao = ""
    sign = ""
    profession = ""
    region = ""
    mail = ""

    def __int__(self):
        return self.id
