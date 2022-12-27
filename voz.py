from gtts import gTTS
from playsound import playsound

s = gTTS("Actualizacion del sistema, actualizacion programada", lang="es-us")
s.save('sample.mp3')
playsound('sample.mp3')