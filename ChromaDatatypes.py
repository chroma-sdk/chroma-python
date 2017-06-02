from time import sleep
import threading
import requests
from typing import List

def checkresult(result):
    try:
        if result["result"] == 0:
            return True, result["result"]
        else:
            return False, result["result"]
    except:
        print("Unexpected Error!")
        raise



class Heartbeat(object):
    def __init__(self, URI=str):
        try:
            self.URI = URI
            self.go = True
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()
        except:
            print("Unexpected Error!")
            raise

    def stop(self):
        self.go = False

    def run(self):
        try:
            while self.go:
                print(requests.put(self.URI + "/heartbeat").json());
                sleep(1)
        except:
            print("Unexpected Error!")
            raise


class ChromaAppInfo:
    Title = ""
    Description = ""
    DeveloperName = ""
    DeveloperContact = ""
    SupportedDevices = []
    Category = ""


class ChromaKey:
    def __init__(self, Key, Color):
        try:
            self._Key = Key
            self._Color = Color
        except:
            print("Unexpected Error!")
            raise

class ChromaColor:
    red = 0
    blue = 0
    green = 0

    def __init__(self, red=None, green=None, blue=None, hex=None):
        try:
            if None in (red, blue, green) and hex is not None:
                if hex[0] == "#":
                    color = hex[1:]
                elif hex[0] == "0" and hex[1] == "x":
                    color = hex[2:]
                else:
                    raise ValueError("Is not Hex-Value!")
                tmp = int(color, 16)

                self.blue = tmp & 255
                self.green = (tmp >> 8) & 255
                self.red = (tmp >> 16) & 255

            elif None not in (red,blue,green) and hex is None:
                if red not in range(0,256):
                    raise ValueError("Red-value out of range!")
                if green not in range(0,256):
                    raise ValueError("Green-value out of range!")
                if blue not in range(0,256):
                    raise ValueError("Blue-value out of range!")
                self.blue = blue
                self.red = red
                self.green = green

            else:
                print("Unexpected Error!")
                raise
        except:
            print("Unexpected Error!")
            raise
    def set(self,red=None,green=None,blue=None,hex=None):
        try:
            if None in (red, blue, green) and hex is not None:
                if hex[0] == "#":
                    color = hex[1:]
                elif hex[0] == "0" and hex[1] == "x":
                    color = hex[2:]
                else:
                    raise ValueError("Is not Hex-Value!")
                tmp = int(color, 16)

                self.blue = tmp & 255
                self.green = (tmp >> 8) & 255
                self.red = (tmp >> 16) & 255
            elif None not in (red,blue,green) and hex is None:
                if red not in range(0,256):
                    raise ValueError("Red-value out of range!")
                if green not in range(0,256):
                    raise ValueError("Green-value out of range!")
                if blue not in range(0,256):
                    raise ValueError("Blue-value out of range!")
                self.blue = blue
                self.red = red
                self.green = green
            else:
                print("Unexpected Error!")
                raise
        except:
            print("Unexpected Error!")
            raise
    def getRGB(self):
        try:
            return self.red, self.green, self.blue
        except:
            print("Unexpected Error!")
            raise

    def getHexBGR(self):
        try:
            return '%02x%02x%02x' % (self.blue, self.green, self.red)
        except:
            print("Unexpected Error!")
            raise

    def getHexRGB(self):
        try:
            return '%02x%02x%02x' % (self.red, self.green, self.blue)
        except:
            print("Unexpected Error!")
            raise