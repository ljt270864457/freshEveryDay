#coding=utf-8
import hashlib 

# 将手机号中间四位设置为*
def formatPhoneNumber(phone):
    return phone[0:3] + '*'*4 + phone[7:11]

# 将密码进行md5加密
def to_md5(string):
    result = hashlib.md5(string)
    return result

if __name__ == '__main__':
    print(to_md5('avcaweq'))