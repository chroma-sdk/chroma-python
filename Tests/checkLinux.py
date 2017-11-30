from ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid
from time import sleep

Info = ChromaAppInfo()
Info.DeveloperName = 'Rick Sanchez'
Info.DeveloperContact = 'Wubba-lubba@dub-dub.com'
Info.Category = 'application'
Info.SupportedDevices = ['keyboard', 'mouse', 'mousepad']
Info.Description = 'Oh Rick, I don\'t know if that\'s a good idea.'
Info.Title = 'Mr Meeseeks Box'

App = ChromaApp(Info)

sleep(2)

print('\n')

print('Setting Keyboard to green')

print(App.Keyboard.setStatic(Colors.GREEN))
sleep(2)
# Oldschool
# KeyboardGrid = [[ChromaColor(red=255, blue=0, green=0) for x in range(22)] for y in range(6)]
# New
KeyboardGrid = ChromaGrid('Keyboard')
print('Setting all devices to red')
KeyboardGrid.set(hexcolor="#FF0000")
print(App.Keyboard.setCustomGrid(KeyboardGrid))
print(App.Keyboard.applyGrid())

sleep(2)

print('Starting animations')

print('Running keyboard-animation')
for i in range(0, len(KeyboardGrid)):
    for j in range(0, len(KeyboardGrid[i])):
        KeyboardGrid[i][j].set(red=255, green=255, blue=0)
        App.Keyboard.setCustomGrid(KeyboardGrid)
        App.Keyboard.applyGrid()
        sleep(0.1)

sleep(2)

print("Setting all devices to none")
App.Keyboard.setNone()

print("If you reached this point, everything seems to be working :)")
sleep(2)
