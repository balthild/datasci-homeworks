import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame, read_csv, Series


def autolabel(rects):
    """
    https://matplotlib.org/examples/api/barchart_demo.html
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., height + 0.1,
                 '%d' % int(height),
                 ha='center', va='bottom')


mpl.rcParams['font.family'] = 'FandolHei'

for cl in ['三5', '三8', '三9']:
    os.makedirs(f'graphs/{cl}', exist_ok=True)

    data: DataFrame = read_csv(f'{cl}.csv')
    avg_list: list = []

    for row in data.iterrows():
        series = row[1]
        name: str = series['姓名']
        num: str = series['考号']
        scores: Series = series[data.columns[5:]]

        plt.xticks(rotation=90)
        plt.ylim((0, 100))

        plt.plot(scores.index, scores.values, marker='o')
        plt.title(num)

        plt.tight_layout()
        plt.savefig(f'graphs/{cl}/{name}.png', dpi=300)
        plt.close()

        print(f'Plotted {cl} {name} {num}')

        avg_list.append(np.array(scores.values).mean())

    avg: np.ndarray = np.array(avg_list)
    avg.sort()

    split_at = avg.searchsorted(range(10, 91, 10))
    intervals: np.ndarray = np.split(avg, split_at)

    r = plt.bar([f'{x}+' for x in range(0, 91, 10)], [y.size for y in intervals])
    autolabel(r)

    plt.title(cl)
    plt.ylabel('Distributions')

    plt.tight_layout()
    plt.savefig(f'graphs/{cl}_dist.png', dpi=300)
    plt.close()

    print(f'Plotted distributions of {cl}')
