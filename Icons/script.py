import os
import json

def create_json_from_svg_folder(folder_path, output_json_path):
    # Ordnername (festgelegt)
    folder_name = "table"

    # Erstelle ein leeres Wörterbuch, um die Ergebnisse zu speichern
    result_dict = {}

    # Durchsuche den angegebenen Ordner nach SVG-Dateien
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".svg"):
            # Extrahiere den Icon-Namen aus dem Dateinamen
            icon_name = os.path.splitext(filename)[0]

            # Erstelle den Schlüssel-Wert-Paar im gewünschten Format
            key = f"{folder_name}-{icon_name}"
            value = f"{folder_name}/filled/{filename}"
            result_dict[key] = value

    # Speichere das Wörterbuch als JSON-Datei
    with open(output_json_path, "w") as json_file:
        json.dump(result_dict, json_file, separators=(',', ':'))

    print("JSON-Datei wurde erfolgreich erstellt: output.json")

# Beispielaufruf mit einem Ordnerpfad
folder_path = "C:/Users/EMGZ2E/Git-Repositories/icon-repo/Icons/table/filled"
output_json_path = "C:/Users/EMGZ2E/Git-Repositories/icon-repo/Icons/output.json"
create_json_from_svg_folder(folder_path, output_json_path)