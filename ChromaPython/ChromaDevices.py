import requests

from .ChromaDatatypes import ChromaColor, checkresult
from .ChromaEnums import KeyboardKeys
from .ChromaBinary import ChromaAnimation
from time import sleep


class Mousepad:
    def __init__(self, uri: str):
        self._MaxLED = 15
        self._ColorGrid = [ChromaColor(red=0, green=0, blue=0) for x in range(15)]
        try:
            self._URI = uri + '/mousepad'

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxLED(self):
        return self._MaxLED

    def setStatic(self, color: ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):

        data = {
            "effect": "CHROMA_NONE"
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setCustomGrid(self, grid):
        try:
            for x in range(0, len(self._ColorGrid)):
                self._ColorGrid[x].set(red=grid[x]._red, green=grid[x]._green, blue=grid[x]._blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def applyGrid(self):

        tmp = [0 for x in range(15)]

        for x in range(0, len(self._ColorGrid)):
            tmp[x] = int(self._ColorGrid[x].getHexBGR(), 16)

        data = {
            "effect": "CHROMA_CUSTOM",
            "param": tmp
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, color: ChromaColor, x=0):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[x].set(red=red, green=green, blue=blue)

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class Headset:
    def __init__(self, uri: str):

        self._MaxLED = 2
        self._ColorGrid = [ChromaColor(red=0, green=0, blue=0) for x in range(2)]
        try:
            self._URI = uri + '/headset'
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxLED(self):
        return self._MaxLED

    def setStatic(self, color: ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):
        data = {
            "effect": "CHROMA_NONE"
            }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setCustomGrid(self, grid):
        try:
            for x in range(0, len(self._ColorGrid)):
                self._ColorGrid[x].set(red=grid[x]._red, green=grid[x]._green, blue=grid[x]._blue)

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def applyGrid(self):

        tmp = [0 for x in range(2)]

        for x in range(0, len(self._ColorGrid)):
            tmp[x] = int(self._ColorGrid[x].getHexBGR(), 16)

        data = {
            "effect": "CHROMA_CUSTOM",
            "param": tmp
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, color: ChromaColor, x=0):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[x].set(red=red, green=green, blue=blue)

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class ChromaLink:
    def __init__(self, uri: str):
        self._MaxLED = 5
        self._ColorGrid = [ChromaColor(red=0, green=0, blue=0) for x in range(5)]

        try:
            self._URI = uri + '/chromalink'


        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxLED(self):
        return self._MaxLED

    def setStatic(self, color: ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):

        data = {
            "effect": "CHROMA_NONE"
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setCustomGrid(self, grid):
        try:
            for x in range(0, len(self._ColorGrid)):
                self._ColorGrid[x].set(red=grid[x]._red, green=grid[x]._green, blue=grid[x]._blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def applyGrid(self):

        tmp = [0 for x in range(5)]

        for x in range(0, len(self._ColorGrid)):
            tmp[x] = int(self._ColorGrid[x].getHexBGR(), 16)

        data = {
            "effect": "CHROMA_CUSTOM",
            "param": tmp
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, color: ChromaColor, x=0):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[x].set(red=red, green=green, blue=blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class Mouse:
    def __init__(self, uri: str):
        self._MaxRow = 9
        self._MaxColumn = 7
        self._ColorGrid = [[ChromaColor(red=0, green=0, blue=0) for x in range(7)] for y in range(9)]

        try:
            self._URI = uri + '/mouse'

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxRow(self):
        return self._MaxRow

    @property
    def MaxColumn(self):
        return self._MaxColumn

    def setStatic(self, color: ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):

        data = {
            "effect": "CHROMA_NONE"
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setCustomGrid(self, grid):
        try:
            for i in range(0, len(self._ColorGrid)):
                for j in range(0, len(self._ColorGrid[i])):
                    self._ColorGrid[i][j].set(red=grid[i][j]._red, green=grid[i][j]._green, blue=grid[i][j]._blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def applyGrid(self):

        tmp = [[0 for x in range(7)] for y in range(9)]

        for i in range(0, len(self._ColorGrid)):
            for j in range(0, len(self._ColorGrid[i])):
                tmp[i][j] = int(self._ColorGrid[i][j].getHexBGR(), 16)

        data = {
            "effect": "CHROMA_CUSTOM2",
            "param": [tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], tmp[8]]
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, color: ChromaColor, x=0, y=0):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[y][x].set(red=red, green=green, blue=blue)
            return True

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class Keyboard:
    def __init__(self, uri: str):
        self._MaxRow = 6
        self._MaxColumn = 22
        self._ColorGrid = [[ChromaColor(red=0, green=0, blue=0) for x in range(22)] for y in range(6)]
        self._Keys = KeyboardKeys()

        try:
            self._URI = uri + '/keyboard'

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxRow(self):
        return self._MaxRow

    @property
    def MaxColumn(self):
        return self._MaxColumn

    def setStatic(self, color: ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):

        data = {
            "effect": "CHROMA_NONE"
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setCustomGrid(self, grid):
        try:
            for i in range(0, len(self._ColorGrid)):
                for j in range(0, len(self._ColorGrid[i])):
                    self._ColorGrid[i][j].set(red=grid[i][j]._red, green=grid[i][j]._green, blue=grid[i][j]._blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def applyGrid(self):

        tmp = [[0 for x in range(22)] for y in range(6)]

        for i in range(0, len(self._ColorGrid)):
            for j in range(0, len(self._ColorGrid[i])):
                tmp[i][j] = int(self._ColorGrid[i][j].getHexBGR(), 16)

        data = {
            "effect": "CHROMA_CUSTOM",
            "param": [tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]]
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, color: ChromaColor, x=0, y=0):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[y][x].set(red=red, green=green, blue=blue)
            return True

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setCustomKey(self, key=None, keys=None):
        try:
            if keys is not None:
                for item in keys:
                    row = int(item._Key, 16) >> 8
                    col = int(item._Key, 16) & 0xFF

                    red, green, blue = item._Color.getRGB()
                    self._ColorGrid[row][col].set(red=red, green=green, blue=blue)

            if key is not None:
                row = int(int(key._Key, 16) >> 8)
                col = int(int(key._Key, 16) & 0xFF)

                red, green, blue = key._Color.getRGB()
                self._ColorGrid[row][col].set(red=red, green=green, blue=blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def playAnimation(self, animation: ChromaAnimation):
        for i in range(0, len(animation.Frames)):
            self.setCustomGrid(animation.Frames[i])
            self.applyGrid()
            sleep(1 / animation.FPS)


class Keypad:
    def __init__(self, uri: str):
        self._MaxRow = 4
        self._MaxColumn = 5
        self._ColorGrid = [[ChromaColor(red=0, green=0, blue=0) for x in range(22)] for y in range(6)]
        self._Keys = KeyboardKeys()

        try:
            self._URI = uri + '/keypad'

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxRow(self):
        return self._MaxRow

    @property
    def MaxColumn(self):
        return self._MaxColumn

    def setStatic(self, color: ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):

        data = {
            "effect": "CHROMA_NONE"
        }

        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setCustomGrid(self, grid):
        try:
            for i in range(0, len(self._ColorGrid)):
                for j in range(0, len(self._ColorGrid[i])):
                    self._ColorGrid[i][j].set(red=grid[i][j]._red, green=grid[i][j]._green, blue=grid[i][j]._blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def applyGrid(self):
        tmp = [[0 for x in range(22)] for y in range(6)]

        for i in range(0, len(self._ColorGrid)):
            for j in range(0, len(self._ColorGrid[i])):
                tmp[i][j] = int(self._ColorGrid[i][j].getHexBGR(), 16)

        data = {
            "effect": "CHROMA_CUSTOM",
            "param": [tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]]
        }
        try:
            return checkresult(requests.put(url=self._URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, color: ChromaColor, x=0, y=0):
        try:
            red, green, blue = color.getRGB()
            self._ColorGrid[y][x].set(red=red, green=green, blue=blue)
            return True

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise
