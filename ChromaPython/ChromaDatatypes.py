from time import sleep
import threading
import requests


def checkresult(result):
    try:
        if result['result'] == 0:
            return True, result['result']
        else:
            return False, result['result']
    except:
        print('Unexpected Error!')
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
            print('Unexpected Error!')
            raise

    def stop(self):
        self.go = False

    def run(self):
        try:
            while self.go:
                requests.put(self.URI + '/heartbeat').json()
                sleep(1)
        except:
            print('Unexpected Error!')
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
            print('Unexpected Error!')
            raise


class ChromaColor:
    _red = 0
    _blue = 0
    _green = 0

    def __init__(self, red=None, green=None, blue=None, hexcolor=None):
        try:
            self.set(red=red,green=green,blue=blue,hexcolor=hexcolor)

        except:
            print("Unexpected Error!")
            raise

    def set(self, red=None, green=None, blue=None, hexcolor=None):
        try:
            if None in (red, blue, green) and hexcolor is not None:
                if hexcolor[0] == '#':
                    color = hexcolor[1:]
                elif hexcolor[0] == '0' and hexcolor[1] == 'x':
                    color = hexcolor[2:]
                else:
                    raise ValueError('Is not Hex-Value!')
                tmp = int(color, 16)

                self._blue = tmp & 255
                self._green = (tmp >> 8) & 255
                self._red = (tmp >> 16) & 255
            elif None not in (red, blue, green) and hexcolor is None:
                if red not in range(0, 256):
                    raise ValueError('Red-value out of range!')
                if green not in range(0, 256):
                    raise ValueError('Green-value out of range!')
                if blue not in range(0, 256):
                    raise ValueError('Blue-value out of range!')
                self._blue = blue
                self._red = red
                self._green = green
                return True
        except:
            print('Unexpected Error!')
            raise

    def getRGB(self):
        try:
            return self._red, self._green, self._blue
        except:
            print('Unexpected Error!')
            raise

    def getHexBGR(self):
        try:
            return '%02x%02x%02x' % (self._blue, self._green, self._red)
        except:
            print('Unexpected Error!')
            raise

    def getHexRGB(self):
        try:
            return '%02x%02x%02x' % (self._red, self._green, self._blue)
        except:
            print('Unexpected Error!')
            raise
