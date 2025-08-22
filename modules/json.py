import os
import json
from typing import Dict, List, Optional, Any, Union, Callable


JSON_CUENTAS = "/home/camper/borradores/proyecto__/Proyecto_Python_Zabala_Nicolas_Medina_Tomas/data/json_cuentas.json"


def ReadJson(file_path: str)-> Dict:
    try:
        with open(file_path, "r", encoding="utf-8") as ArchivoJson:
            return json.load(ArchivoJson)
    except FileExistsError:
        return{}
    
def WriteJson(file_path: str, data: Dict) -> None:
    with open(file_path, "w", encoding="utf-8") as ArchivoJson:
        json.dump(data, ArchivoJson, indent=4)

def UpdateJson(file_path: str, data: Dict, path: Optional[list[str]] = None) -> None:
    CurrentData = ReadJson(file_path)
    if not path:
        CurrentData.update(data)
    else:
        current = CurrentData
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[:-1], {}).update(data
    WriteJson(file_path, CurrentData))
