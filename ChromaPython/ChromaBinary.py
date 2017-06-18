import struct
from enum import Enum
from .ChromaDatatypes import ChromaColor

class ChromaAnimation:
    def __init__(self):
        self.FPS = 0
        self.Frames = []

class BinaryFile:

    class FileHeader:
        def __init__(self):
            self.HEADERSIZE = 14
            self.ftype = 0
            self.fsize = 0
            self.fReserved = 0
            self.fBcaOffset = 0

    class BcaHeader:
        def __init__(self):
            self.hSize = 0
            self.hVersion = 0
            self.hFrameOffset = 0
            self.hFPS = 0
            self.hFrameCount = 0
            self.hReserved = 0

    class FrameHeader:
        def __init__(self):
            self.fhSize = 0
            self.fhDeviceCount = 0
            self.fhDataSize = 0

    class DeviceHeader:
        def __init__(self):
            self.dhSize = 0
            self.dhDatatype = 0
            self.dhDevice = 0
            self.dhDataSize = 0

    class DeviceData:
        def __init__(self):
            self.dRow = 0
            self.dCol = 0
            self.dABGR = 0

    class DeviceType(Enum):

        none = 0x0
        Keyboard = 0x1
        Keypad = 0x2
        Mouse = 0x3
        Mousepad = 0x4
        Headset = 0x5

    class DataType(Enum):
        AssignAll = 0
        AssignNamed = 1

    def __init__(self):
        self.BHeader = self.BcaHeader()
        self.FHeader = self.FileHeader()
        self.FrameList = []


class BinaryDevice:
    def __init__(self):
        self.DeviceHeader = BinaryFile.DeviceHeader()
        self.DeviceDataList = []


class BinaryFrame:
    def __init__(self):

        self.FrameHeader = BinaryFile.FrameHeader()
        self.DeviceList = []


def read_bca(filename):
    with open(filename, "rb") as f:
        file = BinaryFile()

        """Reading FileHeader"""
        file.FHeader.ftype = struct.unpack("<H", f.read(2))[0]
        file.FHeader.fsize = struct.unpack("<L", f.read(4))[0]
        file.FHeader.fReserved = struct.unpack("<L", f.read(4))[0]
        file.FHeader.fBcaOffset = struct.unpack("<L", f.read(4))[0]
        """Reading BCAHeader"""
        file.BHeader.hSize = struct.unpack("<L", f.read(4))[0]
        file.BHeader.hVersion = struct.unpack("<H", f.read(2))[0]
        file.BHeader.hFrameOffset = struct.unpack("<L", f.read(4))[0]
        file.BHeader.hFPS = struct.unpack("<H", f.read(2))[0]
        file.BHeader.hFrameCount = struct.unpack("<L", f.read(4))[0]
        file.BHeader.hReserved = struct.unpack("<H", f.read(2))[0]

        """Reading Frame"""

        for h in range(0, int(file.BHeader.hFrameCount)):

            file.FrameList.append(BinaryFrame())
        for i in range(0, int(file.BHeader.hFrameCount)):
            """Reading FrameHeader"""
            file.FrameList[i].FrameHeader.fhSize = struct.unpack("<H", f.read(2))[0]

            file.FrameList[i].FrameHeader.fhDeviceCount = struct.unpack("<H", f.read(2))[0]
            for j in range(0, file.FrameList[i].FrameHeader.fhDeviceCount):
                file.FrameList[i].DeviceList.append(BinaryDevice())

            file.FrameList[i].FrameHeader.fhDataSize = struct.unpack("<H", f.read(2))[0]
            """Reading Frame Data"""

            for j in range(0, len(file.FrameList[i].DeviceList)):
                file.FrameList[i].DeviceList[j].DeviceHeader.dhSize = struct.unpack("<B", f.read(1))[0]

                file.FrameList[i].DeviceList[j].DeviceHeader.dhDatatype = struct.unpack("<B", f.read(1))[0]

                file.FrameList[i].DeviceList[j].DeviceHeader.dhDevice = struct.unpack("<H", f.read(2))[0]

                file.FrameList[i].DeviceList[j].DeviceHeader.dhDataSize = struct.unpack("<H", f.read(2))[0]

                dataCount = int(file.FrameList[i].DeviceList[j].DeviceHeader.dhDataSize / 6)
                for k in range(0, dataCount):
                    file.FrameList[i].DeviceList[j].DeviceDataList.append(BinaryFile.DeviceData())
                """Reading Device Data"""
                for k in range(0, len(file.FrameList[i].DeviceList[j].DeviceDataList)):
                    file.FrameList[i].DeviceList[j].DeviceDataList[k].dRow = struct.unpack("<B", f.read(1))[0]
                    file.FrameList[i].DeviceList[j].DeviceDataList[k].dCol = struct.unpack("<B", f.read(1))[0]
                    file.FrameList[i].DeviceList[j].DeviceDataList[k].dABGR = struct.unpack("<L", f.read(4))[0]

        return file

def generate_Keyboard_animation(file=BinaryFile):
    animation = ChromaAnimation()
    animation.FPS = file.BHeader.hFPS
    for i in range(0, len(file.FrameList)):
        for j in range(0, len(file.FrameList[i].DeviceList)):
            temp = [[ChromaColor(red=0, green=0, blue=0) for x in range(22)] for y in range(6)]
            if(i > 0):
                for row in range(0,len(animation.Frames[i-1])):
                    for col in range(0,len(animation.Frames[i-1][row])):
                        red, green, blue = animation.Frames[i-1][row][col].getRGB()
                        temp[row][col].set(red=red,blue=blue,green=green)
            if(file.FrameList[i].DeviceList[j].DeviceHeader.dhDevice == 1):
                for k in range(0, len(file.FrameList[i].DeviceList[j].DeviceDataList)):
                    color = file.FrameList[i].DeviceList[j].DeviceDataList[k].dABGR
                    red = (color >> 0) & 255
                    green = (color >> 8) & 255
                    blue = (color >> 16) & 255
                    temp[file.FrameList[i].DeviceList[j].DeviceDataList[k].dRow][
                        file.FrameList[i].DeviceList[j].DeviceDataList[k].dCol].set(red=red,green=green,blue=blue)
                animation.Frames.append(temp)
    return animation






