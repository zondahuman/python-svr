# -*- coding:utf-8 -*-
# !/usr/bin/env python
# https://tracholar.github.io/wiki/python/python-multiprocessing-tutorial.html
import multiprocessing
import time
from com.abin.lee.rabbitmq import TrainSend


def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        # time.sleep(interval)
        TrainSend.assemble()
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.start()
    print "p.pid:", p.pid
    print "p.name:", p.name
    print "p.is_alive:", p.is_alive()