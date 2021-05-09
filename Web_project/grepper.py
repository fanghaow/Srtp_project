#! usr/bin/env python
import requests
import matplotlib.pyplot as plt
import json
import numpy as np

class Web_data(): # Get web data from json file 
    def __init__(self, url = 'http://1.15.140.205/'): # srtp server created by wxf
        self.url = url
        self.download_address = 'http://1.15.140.205/matrix.json'
        self.download_json = "matrix_down.json"
    def web_str(self): # To get web html string
        try:
            print('Start greping web ......')
            str_html = requests.get(self.url)
            str_html.encoding = str_html.apparent_encoding
            str_data = str_html.text
            print('Successfully greped data from url ......')

        except:
            print(Exception)
        # print('data greped from url :', str_data)
        return str_data

    def json_down(self): # Download json file from server and make a transfer
        f = requests.get(self.download_address)
        filename = self.download_address.split('/')
        filename = filename[-1]
        self.json_callback(filename)
        with open(self.download_json, "wb") as jsonfile:
            jsonfile.write(f.content)
        print('Save json file successfully')

    def proceed_json(self): # Proceed local/web json file 
        json_data = open(self.download_json, 'r', encoding='utf-8') 
        l_data_dict = json.load(json_data)
        json_data.close()
        # load data from json data
        time_num = len(l_data_dict)
        wavelength = 256
        l_data_mat = np.zeros((time_num, wavelength))
        for t in range(time_num):
            l_data_mat[t, :] = l_data_dict['Number ' + str(t+1) + ' times']

        # plt.plot(l_data_mat[1, :]) 
        # plt.title('Strength -- Wavelength')
        # plt.xlabel('Wavelength')
        # plt.ylabel('Strength')
        # plt.show()
        return l_data_mat
        
    def caculation(self): # our math model to analyze data
        pass

    def json_callback(self, filename):
        self.download_json = filename

def main():
    wd = web_data()
    # grep web html
    text = wd.web_str() 
    # download json file
    wd.json_down()
    # plot data derived from web
    wd.proceed_json()

if __name__ == '__main__':
    main()
