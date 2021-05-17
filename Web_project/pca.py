import numpy as np
import time

class MY_PCA():
    def __init__(self, mat):
        self.mat = mat
        self.row = mat.shape[0]
        self.col = mat.shape[1]
        pass

    def tf_matrix(self):
        pass

    def zero_mean(self):
        pass

    def covariance(self):
        pass

    def eigenvalue(self):
        pass

    def sort(self):
        pass

    def pca(self):
        pass

def main():
    data = np.zeros((8,6))
    pca = MY_PCA(data)
    t1 = time.time()
    pca.pca()
    t2 = time.time()
    print('It takes me', str(t2-t1), 'seconds to accompish pca!!!')

if __name__ == '__main__':
    main()