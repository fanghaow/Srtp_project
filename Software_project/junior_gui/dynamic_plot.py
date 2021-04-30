# from matplotlib import pyplot as plt
# import numpy as np
#
# x = np.linspace(1, 100, 20)
# y = x * 2 + 3
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.scatter(x, y)
# plt.ion()
# for i in range(10):
#     y = x * i * 0.1 + i
#     try:
#         ax.lines.remove(lines[0])
#     except Exception:
#         pass
#     lines = ax.plot(x, y)
#     plt.pause(0.1)

###
"""
Created on Mon Dec 07 16:34:10 2015

@author: SuperWang
"""

import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()
fig2,ax2=plt.subplots()


y1=[]
y2=[]

for i in range(50):
 y1.append(np.sin(i))
 y2.append(np.cos(i))
 ax.cla()
 ax.set_title("Loss")
 ax.set_xlabel("Iteration")
 ax.set_ylabel("Loss")
 ax.set_xlim(0,55)
 ax.set_ylim(-1,1)
 ax.grid()
 ax.plot(y1,label='train')
 ax.plot(y2,label='test')
 ax.legend(loc='best')

 ax2.cla()
 ax2.set_title("Loss")
 ax2.set_xlabel("Iteration")
 ax2.set_ylabel("Loss")
 ax2.set_xlim(0,55)
 ax2.set_ylim(-1,1)
 ax2.grid()
 ax2.plot(y1,label='train')
 ax2.plot(y2,label='test')
 ax2.legend(loc='best')
 plt.pause(1)