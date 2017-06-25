import requests

class webConnect(object):
    def __init__(self, url, headers, data):
        self.url = url
        self.headers = headers
        self.data = data

    def sendRequest(self):
        requestResponse = requests.post(url=self.url, headers=self.headers, data=self.data)
        return requestResponse

    def getText(self, response):
        return response.text

