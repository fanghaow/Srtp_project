import numpy as np
import matplotlib.pyplot as plt
import xlrd, xlwt
import time
import re

class CaliBration():
    def __init__(self):
        self.path = 'Software_project/junior_gui/DATA/'
        # self.load_label()
        # self.load_txt()
        # self.data_tf()
        # self.predict()

    def load_label(self, grape_num=20, path='Software_project/junior_gui/DATA/', filename='Real_grape.xlsx'):
        self.grape_num = grape_num
        self.pos_num = 3
        label = np.zeros((self.grape_num, self.pos_num))
        filename = path + filename
        ex_file = xlrd.open_workbook(filename)
        table = ex_file.sheet_by_index(0)
        for i in range(self.grape_num):
            for j in range(self.pos_num):
                try:
                    label[i, j] = float(table.cell(i+1, j+1).value)
                    if label[i, j] == 0:
                        label[i, j] = float('inf')
                        print('There is a zero in (%d, %d)' %(i, j))
                except:
                    label[i, j] = float('inf')
                    print('There is a bug in (%d, %d)' %(i, j))
        self.label_mat = label
        # print('Label shape :', self.label.shape)
        return label

    def load_txt(self, grape_num=20, symbol=',', start=0, path='Software_project/junior_gui/DATA/'):
        data_mat = np.zeros((self.grape_num, self.pos_num, 256))
        for i in range(1, grape_num+1):
            for j in range(1, self.pos_num+1):
                file_name = str(i) + '-' + str(j)
                with open(path + file_name + '.txt', encoding = 'utf-8', mode = 'r') as file:
                    data = file.readlines()
                list1 = []
                for line in data:
                    g = re.search(symbol, line)
                    if g:
                        list1.append(list(map(int, line[start:].split(","))))

                mymatrix = np.mat(list1)  # list2matrix
                # print(file_name)
                # print(mymatrix)
                # print('Matrix shape :', mymatrix.shape)
                # print(np.mean(mymatrix, axis=0).shape)
                data_mat[i-1, j-1, :] = np.mean(mymatrix, axis=0)

        # print('Grape data shape:', self.data_mat.shape)
        return data_mat

    def data_tf(self, data_mat, label_mat, needsave=True): 
        # Transform data into modeling size
        wrong_indices = []
        data = np.zeros((self.grape_num * self.pos_num, 256))
        label = np.zeros((self.grape_num * self.pos_num, 1))
        for i in range(self.grape_num):
            for j in range(self.pos_num):
                if self.label_mat[i, j] == float('inf'):
                    wrong_indices.append(i * self.pos_num + j)
                data[i * self.pos_num + j, :] = data_mat[i, j, :]
                label[i * self.pos_num + j, :] = label_mat[i, j]
        if len(wrong_indices) != 0:
            label = np.delete(label, wrong_indices, axis=0)
            data = np.delete(data, wrong_indices, axis=0)
        data = np.hstack((np.ones((self.grape_num * self.pos_num - len(wrong_indices), 1)), data))
        print('After transform, their shape trun to :', data.shape, label.shape)
        if needsave:
            # Save data into excel workbook
            style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',\
                num_format_str='#,##0.00') # ’Times New Roman‘ font
            # style1 = xlwt.easyxf(num_format_str='D-MMM-YY') 
            wb = xlwt.Workbook()
            ws = wb.add_sheet('Sheet1')

            # print(self.data_mat[1, 1, :], '\n', self.data_mat[1, 2, :])
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    ws.write(j, i, data[i, j])
                ws.write(data.shape[1]+3, i, label[i, 0])

            wb.save('Software_project/junior_gui/My_module/Combined_data.xls')
        return data, label

    def PLS(self):
        # Parameters
        params = np.zeros((256+1, 1))


    def OLS(self, data, label):
        # Parameters initial setting
        vector_num = data.shape[1] + 1
        params = np.zeros((vector_num, 1))
        # Analytical solution
        params = np.linalg.pinv(np.dot(data.T, data)) 
        params = np.dot(params, np.dot(data.T, label))
        # print('Parameters :', params)
        # Estimate model
        pre_label = np.dot(data, params)
        # print('Label :', label)
        # print('Predicted label :', pre_label)
        print('Trainging set error between label and predicted label:', np.mean(label) - np.mean(pre_label))
        print('Mean abs error between them :', np.mean(np.abs(pre_label - label)))
        if np.mean(np.abs(pre_label - label)) <= 1e-6:
            print('OLS performs greatly!!!')
        SSR = np.sqrt(np.sum((pre_label - np.mean(label)) ** 2))
        SST = np.sqrt(np.sum((label - np.mean(label)) ** 2))
        R_2 = SSR / SST
        print('R^2 :', R_2)
        # plt.plot(label, 'b', label='Real label')
        # plt.plot(pre_label, 'r', label='Predict label')
        # plt.title('OLS Regression Results')
        # plt.xlabel('Sample order')
        # plt.ylabel('Sweetness')
        # plt.text(13.5, 16.5, "Function: Y = Beta * X, R^2 : " + str(R_2)[:5], size = 12, alpha = 0.75)
        # plt.legend()
        # plt.show()
        return params

    def predict(self, params):
        print('\nStart predicting!!!\n')
        # pre_path = 'Software_project/junior_gui/0519DATA/'
        # label_mat = self.load_label(grape_num=36, path=pre_path, filename='realData0519.xlsx')
        # data_mat = self.load_txt(grape_num=36, path=pre_path)
        # data, label = self.data_tf(data_mat, label_mat, needsave=False)
        # pre_label = np.dot(data, params)
        label_mat = self.load_label()
        data_mat = self.load_txt(symbol='\←◆*', start=17)
        data, label = self.data_tf(data_mat, label_mat)
        print('Test shape :', data.shape, label.shape)
        pre_label = np.dot(data, params)

        print('Test set error between label and predicted label:', np.mean(label) - np.mean(pre_label))
        print('Mean abs error between them :', np.mean(np.abs(pre_label - label)))
        plt.plot(label, 'b', label='Real label')
        plt.plot(pre_label, 'r', label='Predict label')
        plt.legend()
        plt.show()

def OLS_debug():
    # Debugging OLS
    one = np.ones((1, 10))
    x = np.arange(1, 11)
    y = x ** 2
    label = np.reshape((1 + 3 * x + 10 * y + 10 * np.random.rand(1, 10)), (10, 1))
    data = np.vstack((one, x, y))
    print(data)
    print(label.shape)
    cb = CaliBration()
    params = cb.OLS(data.T, label)
    print(params)

def main():
    cb = CaliBration()
    # label_mat = cb.load_label()
    # data_mat = cb.load_txt(symbol='\←◆*', start=17)
    # data, label = cb.data_tf(data_mat, label_mat)
    # params = cb.OLS(data, label)
    # cb.predict(params)

    pre_path = 'Software_project/junior_gui/0519DATA/'
    label_mat = cb.load_label(grape_num=36, path=pre_path, filename='realData0519.xlsx')
    data_mat = cb.load_txt(grape_num=36, path=pre_path)
    data, label = cb.data_tf(data_mat, label_mat, needsave=False)
    print('Training data shape :', data.shape, label.shape)
    params = cb.OLS(data, label)
    cb.predict(params)

if __name__ == '__main__':
    main()
    # OLS_debug()