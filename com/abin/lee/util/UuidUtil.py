# -*- coding:utf-8 -*-
#!/usr/bin/env python
import uuid
import random

def uuid1():
    print u"uuid1  生成基于计算机主机ID和当前时间的UUID"
    return uuid.uuid1() # UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')
def uuid3():
    print u"\nuuid3  基于命名空间和一个字符的MD5加密的UUID"
    return uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org') #UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')
def uuid4():
    print u"\nuuid4  随机生成一个UUID"
    return uuid.uuid4()       #'16fd2706-8baf-433b-82eb-8c7fada847da'
def uuid5():
    print u"\nuuid5  基于命名空间和一个字符的SHA-1加密的UUID"
    return uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org') #UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')
def uuid16():
    print u"\n根据十六进制字符生成UUID"
    x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')
    print u"转换成十六进制的UUID表现字符"
    return str(x)       # '00010203-0405-0607-0809-0a0b0c0d0e0f'

def loanUuidAll():
    unique = str(uuid.uuid1());
    uniqKey = unique.replace('-','')
    return uniqKey


def loanUuid10():
    unique = str(uuid.uuid1());
    uniqKey = unique.replace('-','')
    uniqKey = uniqKey[0:10]
    return uniqKey

def loanUuid15():
    unique = str(uuid.uuid1());
    uniqKey = unique.replace('-','')
    offset = random.randint(10, 15)
    uniqKey = uniqKey[0:offset]
    return uniqKey