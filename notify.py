import subprocess

subprocess.run(
    ["notify-send", "-u", "normal", "-t", "7000", "-i", "dialog-error",
    "NOTIFICACION PRUEBA", "aqui contenido api etc."],
    check=True)