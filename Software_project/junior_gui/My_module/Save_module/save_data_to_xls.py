import xlwt
from datetime import datetime
import numpy as np

wavelength = list(range(256))
data = [float(i) for i in ( np.arange(0,20,256) + np.random.random((256,1)) )]


style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',
    num_format_str='#,##0.00') # ’Times New Roman‘ 字体，红色
style1 = xlwt.easyxf(num_format_str='D-MMM-YY') #

wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet1')

ws.write(0, 0, '波长', style0)
ws.write(0, 1, '反射率', style0)
ws.write(0, 2, '时间', style0)
ws.write(0, 3, '计算量', style0)

for i in range(256):
    ws.write(i+1, 0, 1, style0)
    ws.write(i+1, 1, data[i])
    ws.write(i+1, 2, datetime.now())
    ws.write(i+1, 3, xlwt.Formula('A'+str(i+1)+'+'+'B'+str(i+1)))

wb.save('data.xls')
