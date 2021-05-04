#! usr/bin/env python
import requests
import matplotlib.pyplot as plt
import json

class web_data(): # Get web data from json file 
    def __init__(self, url = 'http://1.15.140.205/'): # srtp server created by wxf
        self.url = url
        self.download_address = 'http://1.15.140.205/array.json'
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
        with open("data_down.json","wb") as jsonfile:
            jsonfile.write(f.content)
        print('Save json file successfully')

    def proceed_json(self): # Proceed local/web json file 
        json_data = open('data_down.json', 'r', encoding='utf-8') # 'array.json' for uploading
        py_list_down = json.load(json_data)
        json_data.close()
        # print(py_list_down)
        wave_length_down = []
        fruit_data_down = []
        for item in py_list_down:
            for key, value in item.items():
                wave_length_down.append(key)
                fruit_data_down.append(value)

        plt.scatter(wave_length_down, fruit_data_down) 
        plt.title('Strength -- Wavelength')
        plt.xlabel('Wavelength')
        plt.ylabel('Strength')
        plt.show()

    def caculation(self): # our math model to analyze data
        pass

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
