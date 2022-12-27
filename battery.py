import os
from gtts import gTTS
from playsound import playsound

def mypass():
        mypass = 'abc1q'
        return mypass

        
def command(cmd):
        global text
        text = os.popen( "echo %s | sudo -S %s" % (mypass(),cmd) ).read()
        print(type(text))
        return text


def escribe_info ():
        with open("example.txt", "w") as f:
                f.write((text))
        


s = gTTS("Actualizacion del sistema, actualizacion programada", lang="es-us")
s.save('sample.mp3')
playsound('sample.mp3')

print (command('acpi -V'))
escribe_info()

