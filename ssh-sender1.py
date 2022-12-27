import os

def mypass():
        mypass = 'abc1q'
        return mypass

        
def command(cmd):
        text = os.popen( "echo %s | sudo -S %s" % (mypass(),cmd) ).read()
        return text

print (command('service ssh status'))
