#! usr/bin/env python
import requests
import matplotlib.pyplot as plt
import json

class web_data(): # Get web data from json file 
    def __init__(self, url = 'http://1.15.140.205/'): # srtp server created by wxf
        self.url = url

    def web_str(self): # To get web html string
        try:
            print('Start greping web ......')
            str_html = requests.get(self.url)
            str_html.encoding = str_html.apparent_encoding
            str_data = str_html.text
            print('Successfully greped data from url ......')

        except:
            print(Exception)

        print('data greped from url :', str_data)
        return str_data

    def json_tf(self): # Download json file from server and make a transfer
        pass

    def sim_json(self): # Proceed local json file 
        # sim_data = 
        pass

    def caculation(self): # our math model to analyze data
        pass

def main():
    wd = web_data()
    text = wd.web_str()

if __name__ == '__main__':
    main()
