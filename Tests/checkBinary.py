from time import sleep
from ChromaPython import ChromaApp,ChromaAppInfo


Info = ChromaAppInfo
Info.DeveloperName = 'Rick Sanchez'
Info.DeveloperContact = 'Wubba-lubba@dub-dub.com'
Info.Category = 'application'
Info.SupportedDevices = ['keyboard','mouse','mousepad']
Info.Description = 'Oh Rick, I don\'t know if that\'s a good idea.'
Info.Title = 'Test'

App = ChromaApp(Info)

sleep(2)

print('If you are interested in the API-version:')
print(App.Version())
print('\n')

print("Reading BCA")
TestBcaFile = App.BcaHandler.decode("Tetris.bca")
print("Generating Animation")
keyboardanimation = App.BcaHandler.generateKeyboardAnimation(TestBcaFile)
print("Playing Animation")
App.Keyboard.playAnimation(keyboardanimation)
