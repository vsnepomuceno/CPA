import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np


def toPercent(vals):
       newVals = list()
       sumValue = sum(vals)
       for i in range(len(vals)):
              print(i)       
              newVals.append((vals[i]/sumValue)*100)
       
       return newVals

def plotChart(labelss, ylabel, title, valuess):

       width = 0.35       

       fig, ax = plt.subplots()
       valuess = toPercent(list(valuess))
       #print(valuess)
       ax.bar(labelss, valuess, width)

       ax.set_ylabel(ylabel)
       ax.set_title(title)
       ax.legend()

       l = list(valuess)
       ls = list(labelss)
       for i in range(len(valuess)):              
              plt.annotate("{:.2f}%".format(l[i]), xy=(ls[i],l[i]), ha='center', va='bottom')

       formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
       ax.yaxis.set_major_formatter(formatter)

       plt.show()

def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate("{:.2f}%".format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom',
                     size=12)

def plotChartDuplo(labels, ylabel, title, values1, values2):

       width = 0.35       
       values1 = toPercent(list(values1))
       values2 = toPercent(list(values2))

       fig, ax = plt.subplots(figsize=(10,7))
       x = np.arange(len(labels))

       rects1 = ax.bar(x - width/2, values1, width, label='TAE')
       rects2 = ax.bar(x + width/2, values2, width, label='Docente')

       ax.set_ylabel(ylabel)
       ax.set_title(title)
       ax.set_xticks(x)
       ax.tick_params(labelsize=18)
       ax.set_xticklabels(labels)
       #ax.set_xticklabels(labels, rotation = 45, ha="right", rotation_mode="anchor")
       ax.legend()
      
       autolabel(rects1, ax)
       autolabel(rects2, ax)

       fig.tight_layout()

       formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
       ax.yaxis.set_major_formatter(formatter)

       plt.show()

def plotChartTriplo(labels, ylabel, title, values1, values2, values3):

       width = 0.2      
       values1 = toPercent(list(values1))
       values2 = toPercent(list(values2))
       values3 = toPercent(list(values3))

       fig, ax = plt.subplots(figsize=(10,7))
       x = np.arange(len(labels))

       rects1 = ax.bar(x - width, values1, width, label='TAE')
       rects2 = ax.bar(x, values2, width, label='Docente')
       rects3 = ax.bar(x + width, values3, width, label='Discente')

       ax.set_ylabel(ylabel)
       ax.set_title(title)
       ax.set_xticks(x)
       ax.tick_params(labelsize=18)
       ax.set_xticklabels(labels)
       #ax.set_xticklabels(labels, rotation = 45, ha="right", rotation_mode="anchor")
       ax.legend()
      
       autolabel(rects1, ax)
       autolabel(rects2, ax)
       autolabel(rects3, ax)

       fig.tight_layout()

       formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
       ax.yaxis.set_major_formatter(formatter)

       plt.show()

def plotChart2(hlabels, ylabel, barLabels, title, valuess):

       width = 0.30       

       fig, ax = plt.subplots()

       
       for i in range(len(barLabels)) :
              ax.bar(hlabels, valuess[i], width, label=barLabels[i])
       
              for j in range(len(hlabels)):              
                     plt.annotate(str(valuess[i][j]), xy=(hlabels[j],valuess[i][j]), ha='center', va='bottom')


       ax.set_ylabel(ylabel)
       ax.set_title(title)
       ax.legend()       

       plt.show()