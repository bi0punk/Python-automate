import subprocess

import os

def mypass():
        mypass = 'abc1q'
        return mypass

        
def command(cmd):
        text = os.popen( "echo %s | sudo -S %s" % (mypass(),cmd) ).read()
        return text
        result = subprocess.run(["notify-send", "-u", "normal", "-t", "7000", "-i", "dialog-error",
        "NOTIFICACION PRUEBA", "aqui contenido api etc."], stderr=subprocess.PIPE, text=True)
        print(result.stderr)


print (command('apt update'))



result = subprocess.run(["notify-send", "-u", "normal", "-t", "7000", "-i", "dialog-error",
    "NOTIFICACION PRUEBA", "aqui contenido api etc."], stderr=subprocess.PIPE, text=True)
print(result.stderr)
