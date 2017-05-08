#! coding:utf-8
import time

def timestamp():
    return int(time.time()*1000)


if __name__ == '__main__':
    print timestamp()