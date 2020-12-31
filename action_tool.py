#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 常用操作动作库

import sys as oSys
import base as oUtils
import random as osRandom  # 随机数

def wait(second=1):
    """休眠，等待执行完.

    Args:
        second ([int]): [休眠时长，单位为秒.] Defaults to 1.
    """    
    oUtils.setSleep(second)
    return

# ---
def keepAlive():
    """
    触摸状态栏防止黑屏
    """
    oUtils.tap(500,5)
    return

# 随机点击某个区域
def tapWithRand(centX,centY,randLen=10):
    """[随机点击某个区域]

    Args:
        centX ([int]): [中心X坐标]
        centY ([int]): [中心Y坐标]
        rangLen (int, optional): [随机取值范围]. Defaults to 10.
    """    
    halfRang = randLen/2
    nTapX = oUtils.getRandom(centX-halfRang, centX+halfRang)
    nTapY = oUtils.getRandom(centY-halfRang, centY+halfRang)

    #执行点击操作.
    oUtils.tap(nTapX, nTapY)
    return

# 随机向上滑动
def moveUpWithRand(centX,centY,randLen=10,moveLen=50,dura=700):
    """[随机向上滑动一段距离]

    Args:
        centX ([int]): [滑动开始的位置]
        centY ([type]): [滑动结束的位置]
        randLen (int, optional): [随机取值的范围]. Defaults to 10.
        moveLen (int, optional): [移动的长度]. Defaults to 50.
        dura (int, optional): [移动所需的时长,单位ms]. Defaults to 700.
    """
    halfRang = randLen/2
    nTapX = oUtils.getRandom(centX-halfRang, centX+halfRang)
    nTapY = oUtils.getRandom(centY-halfRang, centY+halfRang)

    nMoveLen = oUtils.getRandom(moveLen, moveLen+20)
    oUtils.move(nTapX, nTapY, nTapX, nTapY-nMoveLen, dura)
    return

# 随机向下滑动
def moveDownWithRand(centX,centY,randLen=10,moveLen=50,dura=700):
    """[随机向下滑动一段距离]

    Args:
        centX ([int]): [滑动开始的位置]
        centY ([type]): [滑动结束的位置]
        randLen (int, optional): [随机取值的范围]. Defaults to 10.
        moveLen (int, optional): [移动的长度]. Defaults to 50.
        dura (int, optional): [移动所需的时长,单位ms]. Defaults to 700.
    """
    halfRang = randLen/2
    nTapX = oUtils.getRandom(centX-halfRang, centX+halfRang)
    nTapY = oUtils.getRandom(centY-halfRang, centY+halfRang)

    nMoveLen = oUtils.getRandom(moveLen, moveLen+20)
    oUtils.move(nTapX, nTapY, nTapX, nTapY+nMoveLen, dura)
    return

#………………………………………………………………………………………………
if __name__ == "__main__":
    pass

