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

    FrameList = None
    BHeader = None
    FHeader = None

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


class ChromaBcaHandler:
    def decode(self, filename: str):
        try:
            with open(filename, "rb") as f:
                binary_file = BinaryFile()

                """Reading FileHeader"""
                binary_file.FHeader.ftype = struct.unpack("<H", f.read(2))[0]
                binary_file.FHeader.fsize = struct.unpack("<L", f.read(4))[0]
                binary_file.FHeader.fReserved = struct.unpack("<L", f.read(4))[0]
                binary_file.FHeader.fBcaOffset = struct.unpack("<L", f.read(4))[0]
                """Reading BCAHeader"""
                binary_file.BHeader.hSize = struct.unpack("<L", f.read(4))[0]
                binary_file.BHeader.hVersion = struct.unpack("<H", f.read(2))[0]
                binary_file.BHeader.hFrameOffset = struct.unpack("<L", f.read(4))[0]
                binary_file.BHeader.hFPS = struct.unpack("<H", f.read(2))[0]
                binary_file.BHeader.hFrameCount = struct.unpack("<L", f.read(4))[0]
                binary_file.BHeader.hReserved = struct.unpack("<H", f.read(2))[0]

                """Reading Frame"""

                for h in range(0, int(binary_file.BHeader.hFrameCount)):
                    binary_file.FrameList.append(BinaryFrame())
                for i in range(0, int(binary_file.BHeader.hFrameCount)):
                    """Reading FrameHeader"""
                    binary_file.FrameList[i].FrameHeader.fhSize = struct.unpack("<H", f.read(2))[0]

                    binary_file.FrameList[i].FrameHeader.fhDeviceCount = struct.unpack("<H", f.read(2))[0]
                    for j in range(0, binary_file.FrameList[i].FrameHeader.fhDeviceCount):
                        binary_file.FrameList[i].DeviceList.append(BinaryDevice())

                    binary_file.FrameList[i].FrameHeader.fhDataSize = struct.unpack("<H", f.read(2))[0]
                    """Reading Frame Data"""

                    for j in range(0, len(binary_file.FrameList[i].DeviceList)):
                        binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhSize = struct.unpack("<B",
                                                                                                   f.read(1))[0]

                        binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDatatype = struct.unpack("<B",
                                                                                                       f.read(1))[0]

                        binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDevice = struct.unpack("<H",
                                                                                                     f.read(2))[0]

                        binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDataSize = struct.unpack("<H",
                                                                                                       f.read(2))[0]

                        dataCount = int(binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDataSize / 6)
                        for k in range(0, dataCount):
                            binary_file.FrameList[i].DeviceList[j].DeviceDataList.append(BinaryFile.DeviceData())
                        """Reading Device Data"""
                        for k in range(0, len(binary_file.FrameList[i].DeviceList[j].DeviceDataList)):
                            binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dRow = struct.unpack("<B",
                                                                                                          f.read(1))[0]
                            binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dCol = struct.unpack("<B",
                                                                                                          f.read(1))[0]
                            binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dABGR = struct.unpack("<L",
                                                                                                           f.read(4))[0]
                return binary_file
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def encode(self):
        # TODO implement a method to write Bca to file
        pass

    def generateKeyboardAnimation(self, binary_file: BinaryFile):
        try:
            animation = ChromaAnimation()
            animation.FPS = binary_file.BHeader.hFPS
            for i in range(0, len(binary_file.FrameList)):
                for j in range(0, len(binary_file.FrameList[i].DeviceList)):
                    temp = [[ChromaColor(red=0, green=0, blue=0) for x in range(22)] for y in range(6)]
                    if (i > 0):
                        for row in range(0, len(animation.Frames[i - 1])):
                            for col in range(0, len(animation.Frames[i - 1][row])):
                                red, green, blue = animation.Frames[i - 1][row][col].getRGB()
                                temp[row][col].set(red=red, blue=blue, green=green)
                    if (binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDevice == 1):
                        for k in range(0, len(binary_file.FrameList[i].DeviceList[j].DeviceDataList)):
                            color = binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dABGR
                            red = (color >> 0) & 255
                            green = (color >> 8) & 255
                            blue = (color >> 16) & 255
                            temp[binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dRow][
                                binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dCol].set(red=red, green=green,
                                                                                                   blue=blue)
                        animation.Frames.append(temp)
            return animation
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

    def generateKeypadAnimation(self, binary_file=BinaryFile):
        # TODO implement a method to extract the Keypad animation from BinaryFile
        pass

    def generateMouseAnimation(self, binary_file=BinaryFile):
        # TODO implement a method to extract the Mouse animation from BinaryFile
        pass

    def generateMousepadAnimation(self, binary_file=BinaryFile):
        # TODO implement a method to extract the Mousepad animation from BinaryFile
        pass

    def generateHeadsetAnimation(self, binary_file=BinaryFile):
        # TODO implement a method to extract the Headset animation from BinaryFile
        pass
