import json
import requests



class Ingestiones():
    def __init__(self):
        self.ruta_static="src/pad/static/"

    def leer_api(self,url):
        response = requests.get(url)
        return response.json()
    
    def escribir_json(self):
        pass


# vamos a crear una instancia de la clase
ingestion = Ingestiones()
datos_json =ingestion.leer_api("https://extinct-api.herokuapp.com/api/v1/animal/")
print("esta es la ruta estatica :",ingestion.ruta_static)
print("datos json:",datos_json)



        
    