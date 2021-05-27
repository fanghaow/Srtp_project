import numpy as np
import matplotlib.pyplot as plt
import xlrd, xlwt
import time
import re
from sklearn.cross_decomposition import PLSCanonical, PLSRegression, CCA
import csv

class CaliBration():
    def __init__(self):
        self.path = 'Software_project/junior_gui/DATA_0518/'
        # self.load_label()
        # self.load_txt()
        # self.data_tf()
        # self.predict()

    def load_label(self, grape_num=20, path='Software_project/junior_gui/DATA_0518/', filename='Real_grape.xlsx'):
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

    def load_txt(self, grape_num=20, symbol=',', start=0, path='Software_project/junior_gui/DATA_0518/'):
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
            ws = wb.add_sheet('Sheet2')

            # print(self.data_mat[1, 1, :], '\n', self.data_mat[1, 2, :])
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    ws.write(j, i, data[i, j])
                ws.write(data.shape[1]+3, i, label[i, 0])

            wb.save('Software_project/junior_gui/My_module/Combined_data.xls')
            print('Save excel successfully!!!')
        return data, label

    def PLS(self):
        # Parameters
        params = np.zeros((256+1, 1))

        # #############################################################################
        # Dataset based latent variables model

        with open('Software_project/junior_gui/My_modules/Effective_data.csv', 'r') as csv_f:
            csv_wb = csv.reader(csv_f)
            data_lst = []
            for row in csv_wb:
                try:
                    row = [float(i) for i in row]
                except:
                    row = [float(i) for i in row if i != '\ufeff171']
                    row.insert(0, float(171)) # Waiting for edit
                data_lst.append(row)
            csv_f.close()
        data = np.mat(data_lst)
        sample_num, var_num = data.shape
        X = data[:, 0:var_num-1]
        Y = data[:, -1]

        X_train = X[: np.int(sample_num*0.7)]
        Y_train = Y[: np.int(sample_num*0.7)]
        X_test = X[np.int(sample_num*0.7) :]
        Y_test = Y[np.int(sample_num*0.7) :]

        print("Corr(X)")
        print(np.round(np.corrcoef(X.T), 2))
        print("Corr(Y)")
        print(np.round(np.corrcoef(Y.T), 2))

        # # #############################################################################
        # # Canonical (symmetric) PLS

        # # Transform data
        # # ~~~~~~~~~~~~~~
        # plsca = PLSCanonical(n_components=2)
        # plsca.fit(X_train, Y_train)
        # X_train_r, Y_train_r = plsca.transform(X_train, Y_train)
        # X_test_r, Y_test_r = plsca.transform(X_test, Y_test)

        # # Scatter plot of scores
        # # ~~~~~~~~~~~~~~~~~~~~~~
        # # 1) On diagonal plot X vs Y scores on each components
        # plt.figure(figsize=(12, 8))
        # plt.subplot(221)
        # plt.scatter(X_train_r[:, 0], Y_train_r[:, 0], label="train",
        #             marker="o", s=25)
        # plt.scatter(X_test_r[:, 0], Y_test_r[:, 0], label="test",
        #             marker="o", s=25)
        # plt.xlabel("x scores")
        # plt.ylabel("y scores")
        # plt.title('Comp. 1: X vs Y (test corr = %.2f)' %
        #         np.corrcoef(X_test_r[:, 0], Y_test_r[:, 0])[0, 1])
        # plt.xticks(())
        # plt.yticks(())
        # plt.legend(loc="best")

        # plt.subplot(224)
        # plt.scatter(X_train_r[:, 1], Y_train_r[:, 1], label="train",
        #             marker="o", s=25)
        # plt.scatter(X_test_r[:, 1], Y_test_r[:, 1], label="test",
        #             marker="o", s=25)
        # plt.xlabel("x scores")
        # plt.ylabel("y scores")
        # plt.title('Comp. 2: X vs Y (test corr = %.2f)' %
        #         np.corrcoef(X_test_r[:, 1], Y_test_r[:, 1])[0, 1])
        # plt.xticks(())
        # plt.yticks(())
        # plt.legend(loc="best")

        # # 2) Off diagonal plot components 1 vs 2 for X and Y
        # plt.subplot(222)
        # plt.scatter(X_train_r[:, 0], X_train_r[:, 1], label="train",
        #             marker="*", s=50)
        # plt.scatter(X_test_r[:, 0], X_test_r[:, 1], label="test",
        #             marker="*", s=50)
        # plt.xlabel("X comp. 1")
        # plt.ylabel("X comp. 2")
        # plt.title('X comp. 1 vs X comp. 2 (test corr = %.2f)'
        #         % np.corrcoef(X_test_r[:, 0], X_test_r[:, 1])[0, 1])
        # plt.legend(loc="best")
        # plt.xticks(())
        # plt.yticks(())

        # plt.subplot(223)
        # plt.scatter(Y_train_r[:, 0], Y_train_r[:, 1], label="train",
        #             marker="*", s=50)
        # plt.scatter(Y_test_r[:, 0], Y_test_r[:, 1], label="test",
        #             marker="*", s=50)
        # plt.xlabel("Y comp. 1")
        # plt.ylabel("Y comp. 2")
        # plt.title('Y comp. 1 vs Y comp. 2 , (test corr = %.2f)'
        #         % np.corrcoef(Y_test_r[:, 0], Y_test_r[:, 1])[0, 1])
        # plt.legend(loc="best")
        # plt.xticks(())
        # plt.yticks(())
        # plt.show()

        # # #############################################################################
        # # PLS regression, with multivariate response, a.k.a. PLS2

        # n = 1000
        # q = 3
        # p = 10
        # X = np.random.normal(size=n * p).reshape((n, p))
        # B = np.array([[1, 2] + [0] * (p - 2)] * q).T
        # # each Yj = 1*X1 + 2*X2 + noize
        # Y = np.dot(X, B) + np.random.normal(size=n * q).reshape((n, q)) + 5

        # pls2 = PLSRegression(n_components=3)
        # pls2.fit(X, Y)
        # print("True B (such that: Y = XB + Err)")
        # print(B)
        # # compare pls2.coef_ with B
        # print("Estimated B")
        # print(np.round(pls2.coef_, 1))
        # pls2.predict(X)

        # # PLS regression, with univariate response, a.k.a. PLS1

        # n = 1000
        # p = 10
        # X = np.random.normal(size=n * p).reshape((n, p))
        # y = X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n * 1) + 5
        # pls1 = PLSRegression(n_components=3)
        # pls1.fit(X, y)
        # # note that the number of components exceeds 1 (the dimension of y)
        # print("Estimated betas")
        # print(np.round(pls1.coef_, 1))

        # # #############################################################################
        # # CCA (PLS mode B with symmetric deflation)

        # cca = CCA(n_components=2)
        # cca.fit(X_train, Y_train)
        # X_train_r, Y_train_r = cca.transform(X_train, Y_train)
        # X_test_r, Y_test_r = cca.transform(X_test, Y_test)


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
    # pre_path = 'Software_project/junior_gui/DATA_0519/'
    # label_mat = cb.load_label(grape_num=36, path=pre_path, filename='Real_grape.xlsx')
    # data_mat = cb.load_txt(grape_num=36, path=pre_path)
    # data, label = cb.data_tf(data_mat, label_mat, needsave=True)
    # print('Training data shape :', data.shape, label.shape)
    cb.PLS()

if __name__ == '__main__':
    main()
    # OLS_debug()