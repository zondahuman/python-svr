# -*- coding:utf-8 -*-
#!/usr/bin/env python
import random
import time


def timestamp1000():
    return int(time.time()*1000)

def random1000():
    return random.randint(1,1000)

def random100():
    return random.randint(1,100)

def random10():
    return random.randint(1,10)


def randomNumber(param):
    return random.randint(1,param)

def randomNumber(start, end):
    return random.randint(start, end)

if __name__ == '__main__':
    print random.randint(1, 200)

