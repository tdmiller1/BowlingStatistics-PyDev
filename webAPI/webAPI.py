import urllib.request
import json


class WebApi:
    def __init__(self):
        return

    @classmethod
    def get_players(cls):
        url_general = 'http://webApi.tuckermillerdev.com/players/'
        request = urllib.request.urlopen(url_general)
        string = request.read().decode()

        return json.loads(string)

    @classmethod
    def get_player_games(cls,id):
        id = str(id)
        url_general = 'http://webApi.tuckermillerdev.com/player/'+id+'/history'
        request = urllib.request.urlopen(url_general)
        string = request.read().decode()
        playerHistory = json.loads(string)

        return playerHistory['games']