from users.models import UserInfo

def get_myInfo(user):
    UserInfo.id = user.loginid
    UserInfo.username = user.username
    UserInfo.sex = user.sex
    UserInfo.age = user.age
    UserInfo.headportrait = user.headportrait
    UserInfo.phonenumber = user.phonenumber
    UserInfo.address = user.address
    UserInfo.bloodtype = user.bloodtype
    UserInfo.datebirth = user.datebirth
    UserInfo.constellation = user.constellation
    UserInfo.mail = user.mail
    UserInfo.shengxiao = user.shengxiao
    UserInfo.sign = user.sign
    UserInfo.profession = user.profession
    UserInfo.region = user.region
    return UserInfo