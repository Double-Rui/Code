import binascii
from pyDes import des, CBC, ECB, PAD_PKCS5

# def des_encrypt(secret_key, s):
#     iv = secret_key
#     k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
#     en=k.encrypt(s,padmode=PAD_PKCS5)
#     return binascii.b2a_hex(en)
#
# def des_decrypt(secret_key, s):
#     iv = secret_key
#     k=des(secret_key,CBC,iv,pad=None,padmode=PAD_PKCS5)
#     de=k.decrypt(binascii.b2a_hex(s),padmode=PAD_PKCS5)
#     return de


def encryption(num):
    """对数字进行加密解密处理每个数位上的数字变为与7乘积的个位数字，再把每个数位上的数字a变为10-a．"""
    newNum=[]
    for i in str(num):
        if int(i):
            newNum.append(str(10-int(i)*7%10))
        else:
            newNum.append(str(0))

    # print int(''.join(newNum))
    return int(''.join(newNum))



def decryption(num):
    """对数字进行解密处理，把每个数位上的数字乘以7再进行与10求余即可"""
    oldNum = []
    [oldNum.append(str(int(i) * 7 % 10)) for i in str(num)]
    # print int(''.join(oldNum))
    return int(''.join(oldNum))