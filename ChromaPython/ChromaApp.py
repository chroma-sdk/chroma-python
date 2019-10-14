import requests
from .ChromaBinary import ChromaBcaHandler
from .ChromaDevices import Keyboard, Mouse, Mousepad, ChromaLink, Headset
from .ChromaDatatypes import Heartbeat, ChromaAppInfo


class ChromaApp:
    def __init__(self, Info: ChromaAppInfo):
        url = 'http://localhost:54235/razer/chromasdk'
        data = {
            "title": Info.Title,
            "description": Info.Description,
            "author": {
                "name": Info.DeveloperName,
                "contact": Info.DeveloperContact
            },
            "device_supported": Info.SupportedDevices,
            "category": Info.Category
        }
        try:
            response = requests.post(url=url, json=data)
        except Exception as err:
            print('Can\'nt connect to ' + str(url) + '.\nError:' + str(err))
            exit(1)
        response_json = response.json()
        try:
            self.SessionID, self.URI = response_json['sessionid'], response_json['uri']
        except KeyError as err:
            print('Missing sessionid or uri from response.\nError:' + str(err))
            exit(1)
        self.heartbeat = Heartbeat(self.URI)
        self.Keyboard = Keyboard(self.URI)
        self.Mouse = Mouse(self.URI)
        self.Mousepad = Mousepad(self.URI)
        self.Headset = Headset(self.URI)
        self.ChromaLink = ChromaLink(self.URI)
        self.BcaHandler = ChromaBcaHandler()

    def Version(self):
        url = 'http://localhost:54235/razer/chromasdk'
        try:
            response = requests.get(url=url)
        except Exception as err:
            print('Can\'nt connect to ' + str(url) + '.\nError:' + str(err))
            exit(1)
        try:
            return response.json()['version']
        except KeyError as err:
            print('Missing version from response.\nError:' + str(err))
            exit(1)

    def __del__(self):
        print('I\'m dying')
        self.heartbeat.stop()
        requests.delete(self.URI)
