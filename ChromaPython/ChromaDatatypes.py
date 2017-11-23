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
        # TODO Add proper exception handling
        print('Unexpected Error!')
        raise


class Heartbeat(object):
    def __init__(self, URI: str):
        try:
            self.URI = URI
            self.go = True
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()
        except:
            # TODO Add proper exception handling
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
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class ChromaAppInfo:
    def __init__(self):
        # TODO add proper init-function
        pass

    Title = ""
    Description = ""
    DeveloperName = ""
    DeveloperContact = ""
    SupportedDevices = []
    Category = ""


class ChromaColor:
    _red = 0
    _blue = 0
    _green = 0

    def __init__(self, red=None, green=None, blue=None, hexcolor=None):
        try:
            self.set(red=red, green=green, blue=blue, hexcolor=hexcolor)

        except:
            # TODO Add proper exception handling
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
                if not 0 <= red <= 255:
                    raise ValueError('Red-value out of range!')
                if not 0 <= green <= 255:
                    raise ValueError('Green-value out of range!')
                if not 0 <= blue <= 255:
                    raise ValueError('Blue-value out of range!')
                self._blue = blue
                self._red = red
                self._green = green
                return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def getRGB(self):
        try:
            return self._red, self._green, self._blue
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def getHexBGR(self):
        try:
            return '%02x%02x%02x' % (self._blue, self._green, self._red)
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def getHexRGB(self):
        try:
            return '%02x%02x%02x' % (self._red, self._green, self._blue)
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class ChromaKey:
    def __init__(self, Key, Color: ChromaColor):
        try:
            self._Key = Key
            self._Color = Color
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise
