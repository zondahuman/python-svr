# -*- coding:utf-8 -*-
# !/usr/bin/env python

from enum import Enum

class LendEnum(Enum):
    RRD = "RRD"
    YM = "YM"
    TL = "TL"

class LendNum(Enum):
    ONE = 1
    FIVE = 5
    TEN = 10
    HUNDRED = 100
    FIVE_HUNDRED = 500
    THOUSAND = 1000


