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
            if None not in (red, blue, green):
                if not 0 <= red <= 255:
                    raise ValueError('Red-value out of range!')
                if not 0 <= green <= 255:
                    raise ValueError('Green-value out of range!')
                if not 0 <= blue <= 255:
                    raise ValueError('Blue-value out of range!')

                self._red = int(red)
                self._green = int(green)
                self._blue = int(blue)
                return True

            elif hexcolor is not None:
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


class ChromaGrid:
    def __init__(self, type: str):
        self._types = {'Keyboard': [22, 6], 'Mouse': [7, 9], 'Mousepad': [15], 'ChromaLink': [5], 'Keypad': [4, 5],
                       'Headset': [2]}
        try:
            self.rearrange(type=type)
        except:
            raise

    def __getitem__(self, item):
        return self._grid[item]

    def __len__(self):
        return len(self._grid)

    def rearrange(self, type: str):
        if not type in self._types:
            print('Unexpected Error!')
            raise
        else:
            self._type = self._types[type]
        if len(self._type) == 1:
            self._grid = [ChromaColor(red=0, blue=0, green=0) for x in range(self._type[0])]
        else:
            self._grid = [[ChromaColor(red=0, blue=0, green=0) for x in range(self._type[0])] for y in
                          range(self._type[1])]

    def clear(self):

        for y in self._grid:

            if len(self._type) == 1:
                y.set(red=0, blue=0, green=0)
            else:
                for x in y:
                    x.set(red=0, blue=0, green=0)

    def set(self, red=None, green=None, blue=None, hexcolor=None):

        for y in self._grid:

            if len(self._type) == 1:
                y.set(red=red, green=green, blue=blue, hexcolor=hexcolor)
            else:
                for x in y:
                    x.set(red=red, green=green, blue=blue, hexcolor=hexcolor)


class ChromaKey:
    def __init__(self, Key, Color: ChromaColor):
        try:
            self._Key = Key
            self._Color = Color
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise
