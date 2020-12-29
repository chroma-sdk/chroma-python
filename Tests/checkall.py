from ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid
from time import sleep

Info = ChromaAppInfo()
Info.DeveloperName = 'Rick Sanchez'
Info.DeveloperContact = 'Wubba-lubba@dub-dub.com'
Info.Category = 'application'
Info.SupportedDevices = ['keyboard', 'mouse', 'mousepad', 'keypad']
Info.Description = 'Oh Rick, I don\'t know if that\'s a good idea.'
Info.Title = 'Mr Meeseeks Box'

App = ChromaApp(Info)

sleep(2)

print('If you are interested in the API-version:')
print(App.Version())
print('\n')

print('Setting Keyboard to green, Keypad to purple, Mouse to yellow, and Mousepad to blue')

print(App.Keyboard.setStatic(Colors.GREEN))
print(App.Mousepad.setStatic(Colors.BLUE))
print(App.Mouse.setStatic(Colors.YELLOW))
print(App.Keypad.setStatic(Colors.PURPLE))

sleep(2)
# Oldschool
# KeyboardGrid = [[ChromaColor(red=255, blue=0, green=0) for x in range(22)] for y in range(6)]
# MouseGrid = [[ChromaColor(red=255, blue=0, green=0) for x in range(7)] for y in range(9)]
# MousepadGrid = [ChromaColor(red=255, blue=0, green=0) for x in range(15)]
# New
KeyboardGrid = ChromaGrid('Keyboard')
KeypadGrid = ChromaGrid('Keypad')
MouseGrid = ChromaGrid('Mouse')
MousepadGrid = ChromaGrid('Mousepad')

print('Setting all devices to red')
KeyboardGrid.set(hexcolor="#FF0000")
KeypadGrid.set(hexcolor="0xFF0000")
MousepadGrid.set(red=255, blue=0, green=0)
MouseGrid.set(hexcolor="0xFF0000")
print(App.Mousepad.setCustomGrid(MousepadGrid))
print(App.Mouse.setCustomGrid(MouseGrid))
print(App.Keyboard.setCustomGrid(KeyboardGrid))
print(App.Keypad.setCustomGrid(KeypadGrid))
print(App.Mouse.applyGrid())
print(App.Mousepad.applyGrid())
print(App.Keyboard.applyGrid())
print(App.Keypad.applyGrid())

sleep(2)

print('Starting animations')
print('Running mouse-animation')

for i in range(0, len(MouseGrid)):
    for j in range(0, len(MouseGrid[i])):
        MouseGrid[i][j].set(red=255, green=255, blue=0)
        App.Mouse.setCustomGrid(MouseGrid)
        App.Mouse.applyGrid()
        sleep(0.1)

print('Running keyboard-animation')
for i in range(0, len(KeyboardGrid)):
    for j in range(0, len(KeyboardGrid[i])):
        KeyboardGrid[i][j].set(red=255, green=255, blue=0)
        App.Keyboard.setCustomGrid(KeyboardGrid)
        App.Keyboard.applyGrid()
        sleep(0.1)

print('Running keypad-animation')
for i in range(0, len(KeypadGrid)):
    for j in range(0, len(KeypadGrid[i])):
        KeypadGrid[i][j].set(red=255, green=255, blue=0)
        App.Keypad.setCustomGrid(KeypadGrid)
        App.Keypad.applyGrid()
        sleep(0.1)

print('Running mousepad-animation')
for i in range(0, len(MousepadGrid)):
    MousepadGrid[i].set(red=255, green=255, blue=0)
    App.Mousepad.setCustomGrid(MousepadGrid)
    App.Mousepad.applyGrid()
    sleep(0.1)

sleep(2)

print("Setting all devices to none")
App.Keyboard.setNone()
App.Keypad.setNone()
App.Mouse.setNone()
App.Mousepad.setNone()

print("If you reached this point, everything seems to be working :)")
sleep(2)
