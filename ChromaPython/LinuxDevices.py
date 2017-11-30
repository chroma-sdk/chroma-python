from openrazer.client import DeviceManager
from openrazer.client import constants
from .ChromaDatatypes import ChromaColor
from .ChromaBinary import ChromaAnimation
from time import sleep


class LinuxKeyboard(object):
    def __init__(self, device):
        self._device = device
    @property
    def MaxRow(self):
        return self._device.fx.advanced.rows

    @property
    def MaxColumn(self):
        return self._device.fx.advanced.cols

    def setStatic(self, color: ChromaColor):
        try:
            self._device.fx.advanced.matrix.reset()

            red, green, blue = color.getRGB()
            for y in range(self._device.fx.advanced.rows):
                for x in range(self._device.fx.advanced.cols):
                    self._device.fx.advanced.matrix[y, x] = (red, green,blue)

            self._device.fx.advanced.draw()
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def setNone(self):

        self._device.fx.advanced.matrix.reset()
        self._device.fx.advanced.draw()

    def setCustomGrid(self, grid):
        try:
            for i in range(self._device.fx.advanced.rows):
                for j in range(self._device.fx.advanced.cols):
                    self._device.fx.advanced.matrix[i,j] = (grid[i][j]._red, grid[i][j]._green, grid[i][j]._blue)
            return True
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def applyGrid(self):
        self._device.fx.advanced.draw()

    def setPosition(self, color: ChromaColor, x=0, y=0):
        try:

            red, green, blue = color.getRGB()
            self._device.fx.advanced.matrix[x,y] = (red, green, blue)
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
                    self._device.fx.advanced.matrix[row, col] = (red, green, blue)

            if key is not None:
                row = int(int(key._Key, 16) >> 8)
                col = int(int(key._Key, 16) & 0xFF)

                red, green, blue = key._Color.getRGB()
                self._device.fx.advanced.matrix[row, col] = (red, green, blue)
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


class LinuxDevices(object):
    def __init__(self):
        self._device_manager = DeviceManager()
        try:
            self._devices = {device.type: device for device in self._device_manager.devices}
        except:
            print("ChromaPython currently only supports one device of every type in Python")
            raise
        self._keyboard = LinuxKeyboard(self._devices['keyboard'])

    def __del__(self):
        for device in self._devices:
            self._devices[device].fx.wave(constants.WAVE_LEFT)