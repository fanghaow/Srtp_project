from matplotlib import pyplot as plt
import numpy as np
from math import sin
from matplotlib.widgets import Cursor
import xlrd
#
A0 = 590.8939192
B1 = 2.303196492
B2 = -0.0004665871929
B3 = -0.000007877923077
B4 = 3.020550598E-08
B5 = -4.876599743E-11
def wavelength(i):
    wavelength = A0 + B1 * i + B2 * i ** 2 + B3 * i **3 + B4 * i ** 4 + B5 * i ** 5
    return wavelength
x=[0 for i in range(256)]
for i in range(256):
    x[i] = wavelength(i)#获取wavelength数组数据放入数组x



# #读取excel
# excel = xlrd.open_workbook("./光谱仪正确的鲸鱼数据.xlsx") #读取excel文件，相当于打开excel
# sheet = excel.sheet_by_name("Sheet1") #通过sheet页的名字，跳转sheet页
#
# #获取数据
# max_row = sheet.nrows#获取数据的最大行数
# max_col = sheet.ncols#获取最大列数
# y = [0 for i in range(256)]
# for i in range(256):
#     y[i] = sheet.cell_value(0,i)#获取某一列特定行范围的数据③y = sheet.col_values(11, start_rowx=0, end_rowx=256)
# sheet.row_values(2)#获取某一行的数据 #返回第二列的列表
# sheet.cell_value(1,2)#获取某个坐标的值
# print("x数组长度：",len(y))

# python_to_arduino
import serial  # 导入serial库

ser = serial.Serial('/dev/cu.usbmodem1413101', baudrate=9600, bytesize=8, parity='N', stopbits=1,
                    timeout=0.5)  # 打开端口，每一秒返回一个消息 ,设置自己的串口
# try模块用来结束循环（靠抛出异常）
try:
    for i in range(1):
        # 通过电脑端给arduino发送起始命令：'G'
        act = 'G'
        if (act != 'G' ):
            print('请输入正确的字符')
        else:
            ser.write(act.encode())  # 写s字符  需要用 encode 进行编码
        data = []

        # 开始从arduino接收数据
        while(data == []): #直到读到有效数据才停止循环
            a = ser.readline()
            if(str(a,encoding='gbk')!='' and str(a,encoding='gbk')!='\r\n'):
                data.append(str(a,encoding='gbk'))
        yy = data[0].split(',') # 将字符型数据分割成字符型列表
        y = [int(i) for i in yy if i.isdigit()] # 保存整型数据于y中
        y.append(sum(y)/255)
        print(y)
        print(len(y))
except Exception as e:
    print(e)
    ser.close()  # 抛出异常后关闭端口

#
# plt.rcParams['font.family']='SimHei'
plt.rcParams['font.sans-serif']=['Arial Unicode MS']  #mac中文显示方法，跟换字体文件名字可以更改显示出的文字类型
plt.rcParams['axes.unicode_minus']=False

#绘图，设置标签
fig, ax = plt.subplots(figsize=(10,6))
ax.set_title("wavelength——强度")
ax.set_xlabel("wavelength")
ax.set_ylabel("强度")#如若需要散点简单平滑曲线连接图，只要将scatter改成plot即可 plt.plot(x, y)

max_i = y.index(max(y))#获取y[i]最大值对应的i
min_i = y.index(min(y))#获取y[i]最小值对应的i
ax.plot(x, y, color='b', linewidth=0.8, linestyle='-', label='光谱发生相关曲线')
ax.axvline(x=x[max_i],ls="-.",c="red",linewidth=1)#添加垂直直线
ax.axhline(y=max(y),ls="-.",c="red",linewidth=1,label='最大峰峰值')#添加垂直直线
ax.axvline(x=x[min_i],ls="-.",c="green",linewidth=1)#添加垂直直线
ax.axhline(y=min(y),ls="-.",c="green",linewidth=1,label='最大峰峰值')#添加垂直直线
ax.legend(bbox_to_anchor=(0, 1),loc='lower left',framealpha=0.5)#同时画多条曲线 图例设置参考：https://www.cnblogs.com/lfri/p/12248629.html

#x、y轴精度设置
my_x_ticks = np.arange(560,1160, 20)
my_y_ticks = np.arange(min(y)-(max(y)-min(y))*0.1, max(y)+(max(y)-min(y))*0.1, (max(y)-min(y))/20)
plt.xticks(my_x_ticks,rotation=90)
plt.yticks(my_y_ticks)

#网格设置
plt.grid(b=True,
         color='b',
         linestyle='--',
         linewidth=0.5,
         alpha=0.3,
         axis='both',
         which='both')#网格、图例设置参考：https://www.cnblogs.com/zyg123/p/10519588.html

#鼠标滚轮移动实现图像放缩 参考：https://matplotlib.org/users/event_handling.html
def call_back(event):
    axtemp=event.inaxes
    x_min, x_max = axtemp.get_xlim()
    y_min, y_max = axtemp.get_ylim()
    xfanwei = (x_max - x_min) / 10
    yfanwei = (y_max - y_min) / 10
    if event.button == 'up':
        axtemp.set(xlim=(x_min + xfanwei, x_max - xfanwei))
        axtemp.set(ylim=(y_min + yfanwei, y_max - yfanwei))
        #print('up')
    elif event.button == 'down':
        axtemp.set(xlim=(x_min - xfanwei, x_max + xfanwei))
        axtemp.set(ylim=(y_min - yfanwei, y_max + yfanwei))
        #print('down')
    fig.canvas.draw_idle()  # 绘图动作实时反映在图像上
fig.canvas.mpl_connect('scroll_event', call_back) #滚轮移动事件实现反馈
#
def on_press(event):
    print("my position:", event.button,  event.xdata, event.ydata)

fig.canvas.mpl_connect('button_press_event', on_press)#添加新功能：鼠标点击位置的输出
#
h=[]
l=[]
for i in range(1,len(y)-1):
    if (y[i - 1] < y[i] and y[i + 1] < y[i]):
        h.append(y[i])
    elif(y[i-1] > y[i]  and y[i+1] > y[i]):
        l.append(y[i])
if(len(h)==0):
    h.append(max(y))
if(len(l)==0):
    l.append(min(y))
print("极大值：",h)#极大值点
print("极小值：",l)#极小值点

#最大值和最小值的获取及标记
max_peak = max(y)
min_peak = min(y)
print("最大值点坐标：({},{})".format(x[max_i],max(y)))
print("最小值点坐标：({},{})".format(x[min_i],min(y)))
#
cursor = Cursor(ax, useblit=True, color='black', linewidth=0.5)#鼠标跟随十字架，定义颜色粗细
plt.show()