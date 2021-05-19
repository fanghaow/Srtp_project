import re
import numpy as np

file_path = 'Software_project/junior_gui/DATA/'

for i in range(1, 21):
    for j in range(1, 4):
        file_name = str(i) + '-' + str(j)
        with open(file_path + file_name + '.txt', encoding = 'utf-8', mode = 'r') as file:
            data = file.readlines()
        list1 = []
        for line in data:
            g = re.search('\←◆*', line)
            if g:
                list1.append(list(map(int, line[17:].split(","))))

        mymatrix = np.mat(list1)  # list2matrix
        print(file_name)
        print(mymatrix)
        print('Matrix shape :', mymatrix.shape)
