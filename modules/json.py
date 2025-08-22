import os
import json

JSON_CUENTAS = "/home/camper/borradores/proyecto__/Proyecto_Python_Zabala_Nicolas_Medina_Tomas/data/json_cuentas.json"

JSON_CUENTAS_BORRADAS = None    

def ReadJson(file_path: str)-> dict[str, any]:
    try:
        with open(file_path, "r", encoding="utf-8") as ArchivJson:
            return json.load(ArchivJson)
    except(FileExistsError, json.JSONDecodeError):
        return{}
    
def WriteJson(file_path: str, data: dict[str, any]) -> None:
    directory = os.path.dirname(file_path)
    if directory:
        os.makedev(directory, exist_ok=True)
    with open(file_path, "w", encoding="utf-8")  as ArchivoJson:
        json.dump()