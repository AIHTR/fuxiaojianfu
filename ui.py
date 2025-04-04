import tkinter as tk
import zidonghuacaozuo
from tkinter import *
from zidonghuacaozuo import *
from cnpy import 多线程,工具,keyboard
import threading
import time

# pyinstaller -F -w ui.py

# 全局变量，用于跟踪当前正在运行的线程
current_thread = None

def run_function(func, text_widget):
    global current_thread

    # 停止当前正在运行的函数
    stop_event.set()

    # 清除停止事件
    stop_event.clear()

    # 启动新的线程来运行函数
    current_thread = threading.Thread(target=func, args=(text_widget,))
    current_thread.start()

    # 禁用所有按钮
    自动演习按钮.config(state=tk.DISABLED)
    自动竞技按钮.config(state=tk.DISABLED)
    自动推活动图按钮.config(state=tk.DISABLED)
    自动防卫战按钮.config(state=tk.DISABLED)
    自动转盘按钮.config(state=tk.DISABLED)
    停止按钮.config(state=tk.NORMAL)

def stop_functions():
    global current_thread

    # 停止当前正在运行的函数
    stop_event.set()

    # 恢复所有按钮
    自动演习按钮.config(state=tk.NORMAL)
    自动竞技按钮.config(state=tk.NORMAL)
    自动推活动图按钮.config(state=tk.NORMAL)
    自动防卫战按钮.config(state=tk.NORMAL)
    自动转盘按钮.config(state=tk.NORMAL)
    停止按钮.config(state=tk.DISABLED)

拂晓减负 = tk.Tk()
拂晓减负.title("拂晓减负")
拂晓减负.geometry("350x300+10+0")

tk.Label(拂晓减负, text="日志").place(x=125, y=10)
text_widget = tk.Text(拂晓减负, bg = "lightgrey",width=28, height=18)
text_widget.place(x=130, y=30)

自动推活动图按钮 = tk.Button(拂晓减负,text= "自动推活动图", bg="lightblue",width=15, command=lambda: run_function(自动推活动图, text_widget))
自动推活动图按钮.place(x=5, y=140)
自动演习按钮 = tk.Button(拂晓减负,text= "自动演习", bg="lightblue",width=15, command=lambda: run_function(自动演习, text_widget) )
自动演习按钮.place(x=5, y=20)
自动防卫战按钮 = tk.Button(拂晓减负,text= "自动防卫战", bg="lightblue",width=15, command=lambda: run_function(自动防卫战, text_widget))
自动防卫战按钮.place(x=5, y=100)
自动竞技按钮 = tk.Button(拂晓减负,text= "自动竞技", bg="lightblue",width=15, command=lambda: run_function(自动竞技, text_widget))
自动竞技按钮.place(x=5, y=60)
自动转盘按钮 = tk.Button(拂晓减负,text= "自动转盘", bg="lightblue",width=15, command=lambda: run_function(自动转盘, text_widget))
自动转盘按钮.place(x=5, y=180)
停止按钮 = tk.Button(拂晓减负,text= "停止", bg="lightblue",width=15, command=stop_functions, state=tk.DISABLED)
停止按钮.place(x=5, y=220)


tk.mainloop()