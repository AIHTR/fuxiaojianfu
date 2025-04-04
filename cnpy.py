import os
import uuid
import requests
from time import time, sleep, strftime, localtime
import cv2
from random import randint
import numpy as np
import win32api
import win32gui, win32ui, win32con, win32print, win32com.client
import win32process
import pydirectinput
from threading import Thread
from pynput import keyboard


# 安装需要的库
# pip3 install -r requirements.txt

hwnd_map = {}






def get_all_hwnd(hwnd, mouse):
    pass


def 通过名字获取软件句柄(软件名):
    pass

def 获取模拟器操作句柄(hwnd):
    pass

def 获取所有窗口():
    pass


def 获取屏幕分辨率():
    pass

def 截图(范围=None):
    pass







# 图像

def 处理异常(text, e):
    print(f"{text}: {e}")
    raise


class 图像处理类:

    def __init__(self):

        print("初始化图像处理成功")

    def 找图(self, 大图, 小图, 偏移=(0, 0), 相似度=0.9, 灰度=True):
        """
        :param 大图: 屏幕或软件截图
        :param 小图: 要找的图
        :param 相似度: 最低相似度
        :param 偏移: 软件先对屏幕的偏移
        :return: 找图结果或None
        """
        pass


    def 找多图(self, 大图, 小图, 相似度=0.9, 偏移=(0, 0), 灰度=True):
        """
        :param 大图: 屏幕或软件截图
        :param 小图: 要找的图
        :param 相似度: 最低相似度
        :param 偏移: 软件先对屏幕的偏移
        :return: 找图结果或[]
        """
        pass


    def 读取图片(self, filename):
        """
        :param 路径: 图片路径
        :return: 读取后的图片
        """
        pass

    def 展示图片(self, img):
        pass


    def 播放图片(self, 图片, 留存时间=1):

        pass

    def 剪裁图片(self, img, 左上角坐标, 右下角坐标=(0, 0), 矩形大小=(0, 0)):
        """
        :param 图片: 要剪裁的图片
        :param 左上角坐标: 剪裁开始的坐标
        :param 右下角坐标: 剪裁结束的坐标
        :param 矩形大小: 剪裁图片的宽和高
        :return: 剪裁后的图片
        """
        pass


图像处理 = 图像处理类()





class 键盘鼠标类:
    def __init__(self):
        self.窗口位置 = None
        self.按键类型 = "软"
        self.汉子表 = {
            "空格": "space",
            "上": "up",
            "下": "down",
            "左": "left",
            "右": "right",
            "退格": "backspace"
        }
        self.按下的按键 = []


    def 点击键盘(self, 按键, 次数=1):
        pass

    def 按下键盘(self, 按键):
        pass

    def 松开键盘(self, 按键):
        pass

    def 按键状态(self, 按键):
        pass

    def 点击鼠标(self, 左右="左"):
        pass

    def 精准点击(self, 坐标, 左右="左", 窗口位置=None, 高精度=False):
        pass

    def 双击鼠标(self, 左右=None, 延时=0.05):
        pass

    def 范围点击(self, 范围, 左右="左", 窗口位置=None):
        """
        :param 范围: 一个矩形的坐标
        :param 左右: 左 或者 右
        :param 次数: 鼠标点击次数
        :return: None
        """
        pass

    def 拖动鼠标(self, 开始坐标, 结束坐标):
        """
        :param 开始坐标: 坐标或者范围
        :param 结束坐标: 坐标或者范围
        :return:
        """
        pass


    def 按下鼠标(self):
        pass


    def 松开鼠标(self):
        pass


    def 鼠标拖动(self, 坐标1, 坐标2, 偏移=None, 精准点击=False):
        pass


    def 随机坐标(self, x, y):
        pass


    def 移动鼠标(self, x, y, 精准点击=False):
        pass


    def 是汉字(self, word):
        """判断一个unicode是否是汉字"""
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False



    def 获取鼠标位子(self):
        pass


    def 松开所有按键(self):
        pass


    def 停止移动(self):
        pass

键鼠 = 键盘鼠标类()


class 软件类:
    def __init__(self, 软件名, 软件句柄=None, 模拟器=False):
        print(f"当前加载的软件是：{软件名}")
        self.软件名 = 软件名

        if 软件句柄 is None:
            软件句柄 = self.获取软件句柄()
            if 模拟器:
                软件句柄 = self.获取模拟器操作句柄(软件句柄)
        print(软件句柄)
        self.软件句柄 = 软件句柄
        self.窗口位置 = self.获取窗口坐标()

    def 获取模拟器操作句柄(self, 软件句柄):
        pass

    def 截图(self):
        pass


    def 设置窗口大小和位置(self, 大小=(0, 0), 位置=(0, 0)):
        pass


    def 保存截图(self, 位置=None, 名字=""):
        pass


    def 获取软件句柄(self):
        pass


    def 获取窗口坐标(self):
        pass


    def 设置前台(self):
        pass


    def 是否在前台(self):
        pass


class 工具类:
    def __init__(self):
        print("初始化工具箱")
        self.桌面分辨率 = self.获取屏幕分辨率()


    def 通过名字获取软件句柄(self, 软件名):
        pass


    def 获取所有进程句柄和名字(self):
        pass


    def 获取屏幕分辨率(self):
        pass


    def 截取桌面(self):
        pass


    def 等待(self, 秒):
        pass


    def 时间戳(self):
        pass


    def 获取字符时间(self, 时间戳=None):
        pass


    def 打印(self, 文字):
        pass

    def 保存截图(self, 图片, 位置=None, 名字=""):
        pass

    def 开启按键监控(self, 监控函数):
        keyboard.Listener(on_release=监控函数).start()

class 多线程():
    def __init__(self, 线程名, 参数):
        self.线程 = Thread(
            target=线程名,
            args=参数
        )

    def 是否存活(self):
        try:
            return self.线程.is_alive()
        except Exception as e:
            return False

    def 等待(self):
        return self.线程.join()

    def 开始(self):
        return self.线程.start()

工具 = 工具类()
if __name__ == '__main__':
    获取所有窗口()



