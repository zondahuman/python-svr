# -*- coding:utf-8 -*-
#!/usr/bin/env python
import random
import time


def timestamp1000():
    int(time.time()*1000)

def random1000():
    return random.randint(1,1000)



if __name__ == '__main__':
    print random.randint(1, 200)

