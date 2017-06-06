# -*- coding:utf-8 -*-
# !/usr/bin/env python
# https://tracholar.github.io/wiki/python/python-multiprocessing-tutorial.html

import time
import threading
from com.abin.lee.rabbitmq import TrainSend
from com.abin.lee.thread.enums import ApplicationEnum

global TOTAL_NUM
TOTAL_NUM = ApplicationEnum.LendNum.THOUSAND

class TrainThread(threading.Thread):
    def run(self):
        for i in range(5):
            print 'thread {}, @number: {}'.format(self.name, i)
            TrainSend.assemble()
            # time.sleep(1)

def call():
    print "Start main threading"
    # 创建三个线程
    threads = [TrainThread() for i in range(TOTAL_NUM)]
    # 启动三个线程
    for t in threads:
        t.start()

    print "End Main threading"

def callJoin():
    print "Start main threading"

    threads = [TrainThread() for i in range(TOTAL_NUM)]

    for t in threads:
        t.start()

    # 一次让新创建的线程执行 join
    for t in threads:
        t.join()

    print "End Main threading"


def main():
    # print "Start main threading"
    # # 创建三个线程
    # threads = [MyThread() for i in range(3)]
    # # 启动三个线程
    # for t in threads:
    #     t.start()
    #
    # print "End Main threading"
    # call()
    callJoin()


if __name__ == '__main__':
    main()




