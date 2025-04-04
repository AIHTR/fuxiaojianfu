from cnpy import *
from time import *
from tpzy import *
from pyautogui import *
import threading
import tkinter as tk


拂晓 = 软件类(软件名="MuMu模拟器12", 模拟器=True)
键鼠.窗口位置 = 拂晓.窗口位置
截图 = 拂晓.截图()

stop_event = threading.Event()

def 处理获得奖励结果(截图):
    获得奖励结果 = 图像处理.找图(截图, 获得奖励)
    if 获得奖励结果:
        键鼠.精准点击(获得奖励结果["中心点"], 左右="左")
        return True
    return False

def 处理确定结果(截图):
    确定结果 = 图像处理.找图(截图, 确定)
    if 确定结果:
        键鼠.精准点击(确定结果["矩形"], 左右="左")
        return True
    return False

def 处理更换队伍结果(截图):
    更换队伍结果 = 图像处理.找图(截图, 更换队伍)
    if 更换队伍结果:
        sleep(2)
        键鼠.精准点击(更换队伍结果["中心点"], 左右="左")
        return True
    return False

def 处理弹药耗尽结果(截图):
    弹药耗尽结果 = 图像处理.找图(截图, 弹药耗尽)
    if 弹药耗尽结果:
        sleep(2)
        键鼠.精准点击((850,450), 左右="左")
        return True
    return False

def 处理继续结果(截图):
    继续结果 = 图像处理.找图(截图, 继续)
    if 继续结果:
        键鼠.精准点击(继续结果["中心点"], 左右="左")
        return True
    return False

def 处理启航结果(截图):
    启航结果 = 图像处理.找图(截图, 启航)
    if 启航结果:
        键鼠.精准点击(启航结果["中心点"], 左右="左")
        return True
    return False

def 处理更换对手结果(截图):
    更换对手结果 = 图像处理.找图(截图, 更换对手)
    if 更换对手结果:
        sleep(2)
        键鼠.精准点击(更换对手结果["中心点"], 左右="左")
        return True
    return False
def 处理失败结果(截图):
    失败结果 = 图像处理.找图(截图, 失败)
    if 失败结果:
        键鼠.精准点击(失败结果["中心点"], 左右="左")
        return True
    return False

def 处理迎击结果(截图):
    迎击结果 = 图像处理.找图(截图, 迎击)
    if 迎击结果:
        键鼠.精准点击(迎击结果["中心点"], 左右="左")
        return True
    return False

def 处理军衔升级结果(截图):
    军衔升级结果 = 图像处理.找图(截图, 军衔升级)
    if 军衔升级结果:
        键鼠.精准点击(军衔升级结果["中心点"], 左右="左")

        return True
    return False

def 处理胜结果(截图):
    胜结果 = 图像处理.找图(截图, 胜)
    if 胜结果:
        键鼠.精准点击(胜结果["中心点"], 左右="左")
        return True
    return False

def 处理跳过剧情(截图):
    跳过剧情结果 = 图像处理.找图(截图, 跳过剧情)
    if 跳过剧情结果:
        键鼠.精准点击(跳过剧情结果["中心点"], 左右="左")
        sleep(1)
        return True
    return False

def 处理竞技选对手结果():
    截图 = 拂晓.截图()
    竞技选对手结果 = 图像处理.找图(截图, 竞技倒计时)
    钻石段位结果 = 图像处理.找图(截图, 钻石段位)
    未到传说结果 = 图像处理.找图(截图, 未到传说)
    简单对手坐标 = 竞技选对手结果["中心点"][0],竞技选对手结果["中心点"][1]+380
    中等对手坐标 = 竞技选对手结果["中心点"][0],竞技选对手结果["中心点"][1]+200
    困难对手坐标 = 竞技选对手结果["中心点"][0],竞技选对手结果["中心点"][1]+80
    if 竞技选对手结果:
        sleep(1)
        if 钻石段位结果:
            键鼠.精准点击(中等对手坐标, 左右="左")
            return True
        elif not 钻石段位结果 :
            if 未到传说结果:
                键鼠.精准点击(困难对手坐标, 左右="左")
                return True
            else:
                键鼠.精准点击(简单对手坐标, 左右="左")
                return True
    return False


def 自动演习(text_widget):
    i = 0
    A = 0
    while not stop_event.is_set():
        截图 = 拂晓.截图()
        战斗性能结果 = 图像处理.找多图(截图, 战斗性能)
        启航结果 = 图像处理.找图(截图, 启航)
        更换对手结果 = 图像处理.找图(截图, 更换对手)
        继续结果 = 图像处理.找图(截图, 继续)
        确定结果 = 图像处理.找图(截图, 确定)
        获得奖励结果 = 图像处理.找图(截图, 获得奖励)
        失败结果 = 图像处理.找图(截图, 失败)
        军衔升级结果 = 图像处理.找图(截图, 军衔升级)

        if A == 3:
            text_widget.insert(tk.END, "自动演习结束\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
            return
        elif 确定结果:
            处理确定结果(截图)
        elif 军衔升级结果:
            处理军衔升级结果(截图)
            text_widget.insert(tk.END, "军衔提升\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
        elif i == 5 and 更换对手结果:
            键鼠.精准点击(更换对手结果["中心点"], 左右="左")
            while True:
                sleep(1)
                截图 = 拂晓.截图()
                确定结果 = 图像处理.找图(截图, 确定)
                if 确定结果:
                    键鼠.精准点击(确定结果["矩形"], 左右="左")
                    text_widget.insert(tk.END, "更换对手\n")
                    text_widget.see(tk.END)  # 自动滚动到最新输出
                    i = 0
                    A += 1
                    break
                elif not 确定结果:
                    A = 3
                    text_widget.insert(tk.END, "无法更换对手\n")
                    text_widget.see(tk.END)  # 自动滚动到最新输出
                    break
        elif 启航结果:
            处理启航结果(截图)
        elif 获得奖励结果:
            处理获得奖励结果(截图)
            i += 1
            text_widget.insert(tk.END, "演习完成\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
        elif 继续结果:
            处理继续结果(截图)
        elif 失败结果:
            处理失败结果(截图)
            text_widget.insert(tk.END, "演习失败\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
        elif 战斗性能结果:
            for 战斗性能结果坐标 in 战斗性能结果:
                键鼠.精准点击(战斗性能结果坐标["中心点"], 左右="左")
                sleep(1)
                # print(战斗性能结果坐标["中心点"])

def 自动竞技(text_widget):
    while not stop_event.is_set():
        截图 = 拂晓.截图()
        竞技选对手结果 = 图像处理.找图(截图, 竞技倒计时)
        启航结果 = 图像处理.找图(截图, 启航)
        继续结果 = 图像处理.找图(截图, 继续)
        奖励结果 = 图像处理.找图(截图, 获得奖励)
        添加竞技次数判定 = 图像处理.剪裁图片(截图, (610,620), 矩形大小=(60, 50))
        添加竞技次数结果 = 图像处理.找图(添加竞技次数判定, 添加竞技次数)

        if 添加竞技次数结果:
            text_widget.insert(tk.END, "无竞技次数\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
            break
        else:
            if 奖励结果:
                处理获得奖励结果(截图)
                sleep(1)
                text_widget.insert(tk.END, "竞技完成\n")
                text_widget.see(tk.END)  # 自动滚动到最新输出
            elif 继续结果:
                处理继续结果(截图)
                sleep(1)
            elif 启航结果:
                处理启航结果(截图)
            elif 竞技选对手结果:
                处理竞技选对手结果()
                sleep(1)

def 自动防卫战(text_widget):
    while not stop_event.is_set():
        截图 = 拂晓.截图()
        启航结果 = 图像处理.找图(截图, 启航)
        迎击结果 = 图像处理.找图(截图, 迎击)
        继续结果 = 图像处理.找图(截图, 继续)
        防卫战结果 = 图像处理.找图(截图, 防卫战)
        胜结果 = 图像处理.找图(截图, 胜)
        if 防卫战结果:
            text_widget.insert(tk.END, "自动推防卫战结束\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
            return
        elif 启航结果:
            处理启航结果(截图)
        elif 迎击结果:
            处理迎击结果(截图)
        elif 胜结果:
            处理胜结果(截图)
        elif 继续结果:
            处理继续结果(截图)

def 自动推活动图(text_widget):
    i = 0
    while not stop_event.is_set():
        截图 = 拂晓.截图()
        掉落列表结果 = 图像处理.找图(截图, 掉落列表)
        弹药耗尽结果 = 图像处理.找图(截图, 弹药耗尽)
        失败结果 = 图像处理.找图(截图, 失败)
        获得奖励结果 = 图像处理.找图(截图, 获得奖励)
        确定结果 = 图像处理.找图(截图, 确定)
        继续结果 = 图像处理.找图(截图, 继续)
        胜结果 = 图像处理.找图(截图, 胜)
        跳过剧情结果 = 图像处理.找图(截图, 跳过剧情)
        启航结果 = 图像处理.找图(截图, 启航)
        推荐培养结果 = 图像处理.找图(截图, 推荐培养)
        指挥官结果 = 图像处理.找图(截图, 指挥官)

        if 掉落列表结果:
            text_widget.insert(tk.END, "完成推图\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
            break

        elif 弹药耗尽结果:
            处理弹药耗尽结果(截图)
            text_widget.insert(tk.END, "更换队伍\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出

        elif 确定结果:
            处理确定结果(截图)

        elif 跳过剧情结果:
            处理跳过剧情(截图)
            text_widget.insert(tk.END, "跳过剧情\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出

        elif 获得奖励结果:
            处理获得奖励结果(截图)
            sleep(1)
            i = i+1

        elif 继续结果:
            处理继续结果(截图)

        elif 启航结果:
            处理启航结果(截图)

        elif 推荐培养结果:
            键鼠.精准点击(推荐培养结果["中心点"], 左右="左")
            text_widget.insert(tk.END, "获得舰灵\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出

        elif 指挥官结果:
            键鼠.精准点击(指挥官结果["中心点"], 左右="左")

def 自动转盘(text_widget):
    while not stop_event.is_set():
        截图 = 拂晓.截图()
        转盘结果 = 图像处理.找图(截图, 转盘)
        获得奖励结果 = 图像处理.找图(截图, 获得奖励)
        转盘暴击结果 = 图像处理.找图(截图, 转盘暴击)
        抽奖券不足结果 = 图像处理.找图(截图, 抽奖券不足)

        if 抽奖券不足结果:
            处理确定结果(截图)
            text_widget.insert(tk.END, "抽奖券不足\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
            break
        elif 获得奖励结果:
            处理获得奖励结果(截图)
            sleep(1)
        elif 转盘暴击结果:
            键鼠.精准点击(转盘暴击结果["中心点"], 左右="左")
            sleep(1)
            text_widget.insert(tk.END, "转盘暴击\n")
            text_widget.see(tk.END)  # 自动滚动到最新输出
        elif 转盘结果:
            键鼠.精准点击(转盘结果["中心点"], 左右="左")
            sleep(2)
