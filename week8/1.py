# -*- coding: utf-8 -*-

import matplotlib.pylab as pl
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import leastsq


def func(x, p):
    A, k, theta, B = p
    return A * np.sin(np.pi * k * x / 180 + theta) + B


def residuals(p, y, x):
    return y - func(x, p)


x = np.array([0, 3, 6, 9, 12, 15, 18, 21,
              24, 27, 30, 33, 36, 39, 42, 45, 48])
y = np.array([48.5, 52.6, 27.0, -13.8, -38.0, -29.5, -4.9, 25.2,
              48.6, 53.2, 26.7, -16.1, -39.4, -29.9, -3.5, 25.2, 48.5])

p0 = [80, 20, 0, 0]  # 第一次猜测的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(y, x))

print("拟合参数", plsq[0])  # 实验数据拟合后的参数

func_interp = interp1d(x, y, kind='cubic')

pl.rcParams['font.family'] = ['FandolHei']
pl.rcParams['axes.unicode_minus'] = False

xs = np.linspace(0, 48, 100)
pl.scatter(x, y, label=u"实验数据")
pl.plot(xs, func(xs, plsq[0]), label=u"拟合数据")
pl.plot(xs, func_interp(xs), label=u"插值数据")

pl.legend()
pl.show()
