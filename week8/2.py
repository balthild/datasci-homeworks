# -*- coding: utf-8 -*-

import matplotlib.pylab as pl
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit


def func(x, a, b, c):
    return a * np.sin(np.pi / 6 * x + b) + c


x = list(range(1, 13))
max_y = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
min_y = [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]

xl = np.linspace(1, 12, 100)
max_yf = func(xl, *curve_fit(func, x, max_y)[0])
min_yf = func(xl, *curve_fit(func, x, min_y)[0])

pl.rcParams['font.family'] = ['FandolHei']
pl.rcParams['axes.unicode_minus'] = False

pl.plot(xl, max_yf, label=u"最高温度 (拟合)")
pl.plot(xl, min_yf, label=u"最低温度 (拟合)")

pl.scatter(x, max_y, label=u"最高温度")
pl.scatter(x, min_y, label=u"最低温度")

pl.plot(xl, min_yf)

pl.legend()
pl.show()
