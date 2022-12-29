import threading
import time
import urllib.request
import pandas as pd
import requests
import datetime
import subprocess



# Tarea a ejecutarse cada determinado tiempo.
def timer():
    while True:
        try:
            x = requests.get('https://www.sismologia.cl/sismicidad/catalogo/2022/12/20221229.html')
            print(x.status_code)
            code = x.status_code
            if code == 403:
                print("error de pagina")
                time.sleep(600)
                return timer
            
            table_MN = pd.read_html('https://www.sismologia.cl/sismicidad/catalogo/2022/12/20221229.html')
            print(f'Total tables: {len(table_MN)}')
            global df
            df = table_MN[1]
            data_count = df.shape
            print(df)
            contador = 1
            filas = data_count[0]
            if filas != contador:
                print("nuevo registro")
                result = subprocess.run(["notify-send", "-u", "normal", "-t", "7000", "-i", "face-smile","Alerta Sismológica", "UN NUEVO REGISTRO"], stderr=subprocess.PIPE, text=True)
                print(result.stderr)
            
                contador = contador + 1
            if contador == filas:
                print("nada nuevo")
                result = subprocess.run(["notify-send", "-u", "normal", "-t", "7000", "-i", "dialog-error","Alerta Sismológica", "Nada nuevo"], stderr=subprocess.PIPE, text=True)
                print(result.stderr)
            
            print(filas)
            print("")
            print(contador)
            """ df.to_csv('file_name.csv', encoding='utf-8') """
            df.to_csv('datasismos.csv', mode='a', index=False, header=True, encoding='utf-8')
            fecha_data = datetime.datetime.now()
            print("\n")
            print(fecha_data)
            
            time.sleep(600) 
        except:
            print("Error")
        
        
# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()
