import requests

from .ChromaDatatypes import ChromaColor, checkresult
from .ChromaEnums import KeyboardKeys
from .ChromaBinary import ChromaAnimation
from time import sleep


class Mousepad:
    _MaxLED = 15
    _ColorGrid = [ChromaColor(red=0, green=0, blue=0) for x in range(15)]

    def __init__(self, uri=str):
        try:
            self.URI = uri + '/mousepad'


        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxLED(self):
        return self._MaxLED

    def setStatic(self, color=ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):
        try:
            data = {
                "effect": "CHROMA_NONE"
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
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
        try:
            Tmp = [0 for x in range(15)]

            for x in range(0, len(self._ColorGrid)):
                Tmp[x] = int(self._ColorGrid[x].getHexBGR(), 16)

            data = {
                "effect": "CHROMA_CUSTOM",
                "param": Tmp
            }
            return checkresult(requests.put(url=self.URI, json=data).json())

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, x=0, color=None):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[x].set(red=red, green=green, blue=blue)

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class Headset:
    _MaxLED = 2
    _ColorGrid = [ChromaColor(red=0, green=0, blue=0) for x in range(2)]

    def __init__(self, uri=str):
        try:
            self.URI = uri + '/headset'


        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxLED(self):
        return self._MaxLED

    def setStatic(self, color=ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):
        try:
            data = {
                "effect": "CHROMA_NONE"
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
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
        try:
            Tmp = [0 for x in range(2)]

            for x in range(0, len(self._ColorGrid)):
                Tmp[x] = int(self._ColorGrid[x].getHexBGR(), 16)

            data = {
                "effect": "CHROMA_CUSTOM",
                "param": Tmp
            }
            return checkresult(requests.put(url=self.URI, json=data).json())

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, x=0, color=ChromaColor):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[x].set(red=red, green=green, blue=blue)

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class ChromaLink:
    _MaxLED = 5
    _ColorGrid = [ChromaColor(red=0, green=0, blue=0) for x in range(5)]

    def __init__(self, uri=str):
        try:
            self.URI = uri + '/chromalink'


        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    @property
    def MaxLED(self):
        return self._MaxLED

    def setStatic(self, color=ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):
        try:
            data = {
                "effect": "CHROMA_NONE"
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
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
        try:
            Tmp = [0 for x in range(5)]

            for x in range(0, len(self._ColorGrid)):
                Tmp[x] = int(self._ColorGrid[x].getHexBGR(), 16)

            data = {
                "effect": "CHROMA_CUSTOM",
                "param": Tmp
            }
            return checkresult(requests.put(url=self.URI, json=data).json())

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, x=0, color=ChromaColor):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[x].set(red=red, green=green, blue=blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class Mouse:
    _MaxRow = 9
    _MaxColumn = 7
    _ColorGrid = [[ChromaColor(red=0, green=0, blue=0) for x in range(7)] for y in range(9)]

    def __init__(self, uri=str):
        try:
            self.URI = uri + '/mouse'

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

    def setStatic(self, color=ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):
        try:
            data = {
                "effect": "CHROMA_NONE"
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
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
        try:
            Tmp = [[0 for x in range(7)] for y in range(9)]

            for i in range(0, len(self._ColorGrid)):
                for j in range(0, len(self._ColorGrid[i])):
                    Tmp[i][j] = int(self._ColorGrid[i][j].getHexBGR(), 16)

            data = {
                "effect": "CHROMA_CUSTOM2",
                "param": [Tmp[0], Tmp[1], Tmp[2], Tmp[3], Tmp[4], Tmp[5], Tmp[6], Tmp[7], Tmp[8]]
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, x=0, y=0, color=ChromaColor):
        try:

            red, green, blue = color.getRGB()
            self._ColorGrid[y][x].set(red=red, green=green, blue=blue)
            return True

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise


class Keyboard:
    _MaxRow = 6
    _MaxColumn = 22
    _ColorGrid = [[ChromaColor(red=0, green=0, blue=0) for x in range(22)] for y in range(6)]
    _Keys = KeyboardKeys()

    def __init__(self, URI=str):
        try:
            self.URI = URI + '/keyboard'

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

    def setStatic(self, color=ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):
        try:
            data = {
                "effect": "CHROMA_NONE"
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
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
        try:
            Tmp = [[0 for x in range(22)] for y in range(6)]

            for i in range(0, len(self._ColorGrid)):
                for j in range(0, len(self._ColorGrid[i])):
                    Tmp[i][j] = int(self._ColorGrid[i][j].getHexBGR(), 16)

            data = {
                "effect": "CHROMA_CUSTOM",
                "param": [Tmp[0], Tmp[1], Tmp[2], Tmp[3], Tmp[4], Tmp[5]]
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, x=0, y=0, color=ChromaColor):
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

    def playAnimation(self, animation=ChromaAnimation):
        for i in range(0, len(animation.Frames)):
            self.setCustomGrid(animation.Frames[i])
            self.applyGrid()
            sleep(1 / animation.FPS)


class Keypad:
    _MaxRow = 4
    _MaxColumn = 5
    _ColorGrid = [[ChromaColor(red=0, green=0, blue=0) for x in range(22)] for y in range(6)]
    _Keys = KeyboardKeys()

    def __init__(self, URI=str):
        try:
            self.URI = URI + '/keypad'

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

    def setStatic(self, color=ChromaColor):
        try:
            data = {
                "effect": "CHROMA_STATIC",
                "param": {
                    "color": int(color.getHexBGR(), 16)
                }
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):
        try:
            data = {
                "effect": "CHROMA_NONE"
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
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
        try:
            Tmp = [[0 for x in range(22)] for y in range(6)]

            for i in range(0, len(self._ColorGrid)):
                for j in range(0, len(self._ColorGrid[i])):
                    Tmp[i][j] = int(self._ColorGrid[i][j].getHexBGR(), 16)

            data = {
                "effect": "CHROMA_CUSTOM",
                "param": [Tmp[0], Tmp[1], Tmp[2], Tmp[3], Tmp[4], Tmp[5]]
            }
            return checkresult(requests.put(url=self.URI, json=data).json())
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setPosition(self, x=0, y=0, color=ChromaColor):
        try:
            red, green, blue = color.getRGB()
            self._ColorGrid[y][x].set(red=red, green=green, blue=blue)
            return True

        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise
