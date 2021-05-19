import numpy as np
import matplotlib.pyplot as plt
import xlrd
import time
import re

class CaliBration():
    def __init__(self):
        self.path = 'Software_project/junior_gui/DATA/'
        self.load_label()
        self.load_txt()
        self.data_tf()

    def load_label(self):
        self.grape_num = 20
        self.pos = 3
        label = np.zeros((self.grape_num, self.pos))
        filename = self.path + 'Real_grape.xlsx'
        ex_file = xlrd.open_workbook(filename)
        table = ex_file.sheet_by_index(0)
        for i in range(self.grape_num):
            for j in range(self.pos):
                label[i, j] = float(table.cell(i+1, j+1).value)
        self.label_mat = label
        # print('Label shape :', self.label.shape)

    def load_txt(self):
        self.data_mat = np.zeros((self.grape_num, self.pos, 256))
        for i in range(1, 21):
            for j in range(1, 4):
                file_name = str(i) + '-' + str(j)
                with open(self.path + file_name + '.txt', encoding = 'utf-8', mode = 'r') as file:
                    data = file.readlines()
                list1 = []
                for line in data:
                    g = re.search('\←◆*', line)
                    if g:
                        list1.append(list(map(int, line[17:].split(","))))

                mymatrix = np.mat(list1)  # list2matrix
                # print(file_name)
                # print(mymatrix)
                # print('Matrix shape :', mymatrix.shape)
                self.data_mat[i-1, j-1, :] = np.mean(mymatrix)

        # print('Grape data shape:', self.data_mat.shape)

    def data_tf(self): 
        # Transform data into modeling size
        data = np.zeros((self.grape_num * self.pos, 256))
        label = np.zeros((self.grape_num * self.pos, 1))
        for i in range(self.grape_num):
            for j in range(self.pos):
                if self.label_mat[i, j] == 0:
                    wrong_index = i * self.pos + j
                data[i * self.pos + j] = self.data_mat[i, j, :]
                label[i * self.pos + j] = self.label_mat[i, j]
        self.label = np.delete(label, wrong_index, axis=0)
        data = np.hstack((np.ones((self.grape_num * self.pos, 1)), data))
        self.data = np.delete(data, wrong_index, axis=0)
        # print('Their shape :', self.label.shape, self.data.shape)

    def PLS(self):
        # Parameters
        params = np.zeros((256+1, 1))


    def OLS(self):
        # Parameters initial setting
        params = np.zeros((256+1, 1))
        # Analytical solution
        params = np.linalg.pinv(np.dot(self.data.T, self.data)) 
        params = np.dot(params, np.dot(self.data.T, self.label))
        # Estimate model
        pre_label = np.dot(self.data, params)
        print('Error :', np.mean(self.label) - np.mean(pre_label))
        if np.mean(self.label) == np.mean(pre_label):
            print('OLS dubuging successfully!!!')
        SSR = np.sqrt(np.sum((pre_label - np.mean(self.label)) ** 2))
        SST = np.sqrt(np.sum((self.label - np.mean(self.label)) ** 2))
        R_2 = SSR / SST
        print('R^2 :', R_2)
        plt.plot(self.label, 'b', label='Real label')
        plt.plot(pre_label, 'r', label='Predict label')
        plt.title('OLS Regression Results')
        plt.xlabel('Sample order')
        plt.ylabel('Sweetness')
        plt.text(13.5, 16.5, "Function: Y = Beta * X, R^2 : " + str(R_2)[:5], size = 12, alpha = 0.75)
        plt.legend()
        plt.show()

    def predict(self):
        pass

def main():
    cb = CaliBration()
    cb.OLS()

if __name__ == '__main__':
    main()