import urllib.request
import json

class webAPI():
    def __init__(self):
        return

    def getPlayers(self):
        url_general = 'http://webApi.tuckermillerdev.com/players/'
        request = urllib.request.urlopen(url_general)
        string = request.read().decode()

        data = json.loads(string)
        return data