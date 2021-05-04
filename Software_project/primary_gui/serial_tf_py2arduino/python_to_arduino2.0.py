# -*-coding:UTF-8-*-
import serial  # 导入serial库

ser = serial.Serial('COM7', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.5)  # 打开端口，每一秒返回一个消息 ,设置自己的串口
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
        for j in range(1000):
            print(ser.readline())
        # 开始从arduino接收数据

        # while(data == []): #直到读到有效数据才停止循环
        #     a = ser.readline()
        #     if(str(a,encoding='gbk')!='' and str(a,encoding='gbk')!='\r\n'):
        #         data.append(str(a,encoding='gbk'))
        # yy = data[0].split(',') # 将字符型数据分割成字符型列表
        # y = [int(i) for i in yy if i.isdigit()] # 保存整型数据于y中
        # y.append(85)
        # print(y)
        # print(len(y))
except Exception as e:
    print(e)
    ser.close()  # 抛出异常后关闭端口