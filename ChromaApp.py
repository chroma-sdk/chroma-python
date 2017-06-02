import requests
from time import sleep
from ChromaDevices import Keyboard
from ChromaDevices import Mouse
from ChromaDevices import Mousepad
from ChromaDatatypes import Heartbeat, ChromaAppInfo



class ChromaApp:
    heartbeat = None

    def __init__(self, Info=ChromaAppInfo):
        try:
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
            response = requests.post(url=url, json=data)
            self.SessionID, self.URI = response.json()["sessionid"], response.json()["uri"]
            self.heartbeat = Heartbeat(self.URI)
            self.Keyboard = Keyboard(self.URI)
            self.Mouse = Mouse(self.URI)
            self.Mousepad = Mousepad(self.URI)
        except:
            print("Unexpected Error!")
            raise
    def __del__(self):
        print("Im dying")
        self.heartbeat.stop()


