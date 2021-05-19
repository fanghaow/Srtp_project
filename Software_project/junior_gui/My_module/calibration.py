import numpy as np
import matplotlib.pyplot as plt
import xlrd
import time

class CaliBration():
    def __init__(self):
        self.path = 'DATA/'
        self.load_label()

    def load_label(self):
        self.grape_num = 20
        self.pos = 3
        label_mat = np.zeros((self.grape_num, self.pos))
        filename = 'Software_project/junior_gui/DATA/Real_grape.xlsx'
        ex_file = xlrd.open_workbook(filename)
        table = ex_file.sheet_by_index(0)
        for i in range(self.grape_num):
            for j in range(self.pos):
                label_mat[i, j] = float(table.cell(i+1, j+1).value)
        self.label_mat = label_mat

    def load_txt(self):
        pass

    def PLS(self):
        pass

    def predict(self):
        pass

def main():
    cb = CaliBration()
    print(cb.label_mat)

if __name__ == '__main__':
    main()