from time import sleep
from ChromaPython import ChromaApp,ChromaAppInfo, read_bca,generate_Keyboard_animation


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
TestBcaFile = read_bca("Pacman.bca")
print("Generating Animation")
keyboardanimation = generate_Keyboard_animation(TestBcaFile)
print("Playing Animation")
App.Keyboard.playAnimation(keyboardanimation)
