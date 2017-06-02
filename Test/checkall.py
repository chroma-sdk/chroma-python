from ChromaApp import ChromaApp,ChromaAppInfo
from ChromaDatatypes import ChromaColor
from ChromaEnums import Colors
from time import sleep



Info = ChromaAppInfo
Info.DeveloperName = "Rick Sanchez"
Info.DeveloperContact = "Wubba-lubba@dub-dub.com"
Info.Category = "application"
Info.SupportedDevices = ["keyboard,mouse,mousepad"]
Info.Description = "Oh Rick, I don't know if that's a good idea."
Info.Title = ""

App = ChromaApp(Info)

print(App.Keyboard.setStatic(Colors.BLUE))
print(App.Mousepad.setStatic(Colors.BLUE))
print(App.Mouse.setStatic(Colors.BLUE))
sleep(5)
KeyboardGrid = [[ChromaColor(red=255,blue=0,green=0) for x in range(22)] for y in range(6)]
MouseGrid = [[ChromaColor(red=255,blue=0,green=0) for x in range(7)] for y in range(9)]
MousepadGrid = [ChromaColor(red=255,blue=0,green=0) for x in range(15)]



print(App.Mousepad.setCustomGrid(MousepadGrid))
print(App.Mouse.setCustomGrid(MouseGrid))
print(App.Keyboard.setCustomGrid(KeyboardGrid))
print(App.Mouse.applyGrid())
print(App.Mousepad.applyGrid())
print(App.Keyboard.applyGrid())

sleep(2)
print("Starting animation")
for i in range(0,len(MouseGrid)):
    for j in range(0,len(MouseGrid[i])):
        MouseGrid[i][j].set(red=255,green=255,blue=0)
        print(App.Mouse.setCustomGrid(MouseGrid))
        App.Mouse.applyGrid()
        sleep(0.1)

for i in range(0,len(KeyboardGrid)):
    for j in range(0,len(KeyboardGrid[i])):
        KeyboardGrid[i][j].set(red=255,green=255,blue=0)
        print(App.Keyboard.setCustomGrid(KeyboardGrid))
        App.Keyboard.applyGrid()
        sleep(0.1)
for i in range(0,len(MousepadGrid)):
        MousepadGrid[i].set(red=255,green=255,blue=0)
        print(App.Mousepad.setCustomGrid(MousepadGrid))
        App.Mousepad.applyGrid()
        sleep(0.1)
sleep(2)


App.Keyboard.setNone()
App.Mouse.setNone()
App.Mousepad.setNone()

sleep(2)



