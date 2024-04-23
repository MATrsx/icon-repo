import os
import json
import shutil

def create_json_from_svg_folder(folder_path, output_json_path):
    # Ordnername (festgelegt)
    folder_name = "tabler"

    # Erstelle ein leeres Wörterbuch, um die Ergebnisse zu speichern
    result_dict = {}

    # Durchsuche den angegebenen Ordner nach SVG-Dateien
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".svg"):
            # Extrahiere den Icon-Namen aus dem Dateinamen
            icon_name = os.path.splitext(filename)[0]

            # Erstelle den Schlüssel-Wert-Paar im gewünschten Format
            key = f"{folder_name}-outline-{icon_name}"
            value = f"{folder_name}/outline/{filename}"
            result_dict[key] = value

    # Speichere das Wörterbuch als JSON-Datei
    with open(output_json_path, "w") as json_file:
        json.dump(result_dict, json_file, separators=(',', ':'))

    print("JSON-Datei wurde erfolgreich erstellt: output.json")

def create_json_from_png_folder(base_path, output_json_path):
    # Erstelle ein leeres Wörterbuch, um die Ergebnisse zu speichern
    result_dict = {}

    # Durchsuche die Ordnerstruktur nach PNG-Dateien
    for root, dirs, files in os.walk(base_path):
        for filename in files:
            if filename.lower().endswith(".png"):
                # Extrahiere den Icon-Namen aus dem Dateinamen und den Ordnername
                icon_name = os.path.splitext(filename)[0]
                icon_folder = os.path.relpath(root, base_path).replace("\\", "/")
                parent_folder = os.path.basename(os.path.dirname(root))

                # Erstelle den Schlüssel-Wert-Paar im gewünschten Format
                key = f"fluentemoji-3d-{icon_name}"
                value = f"fluentemoji/{os.path.join(icon_folder, filename)}".replace("\\", "/")
                result_dict[key] = value

    # Speichere das Wörterbuch als JSON-Datei
    with open(output_json_path, "w") as json_file:
        json.dump(result_dict, json_file, separators=(',', ':'))

    print("JSON-Datei wurde erfolgreich erstellt:", output_json_path)

def delete_folders(base_path):
    # Durchsuche den Basispfad nach "3D"-Ordnern
    for root, dirs, files in os.walk(base_path):
        if "3D" in dirs:
            icon_folder = os.path.dirname(os.path.join(root, "3D"))
            # Durchsuche das Verzeichnis des "3D"-Ordners nach "Flat" und "High Contrast"
            for folder in ["Flat", "High Contrast"]:
                folder_path = os.path.join(icon_folder, folder)
                if os.path.exists(folder_path):
                    try:
                        shutil.rmtree(folder_path)
                        print(f"Ordner '{folder}' im Icon-Ordner '{icon_folder}' wurde erfolgreich gelöscht.")
                    except Exception as e:
                        print(f"Fehler beim Löschen des Ordners '{folder}' im Icon-Ordner '{icon_folder}': {e}")
                else:
                    print(f"Der Ordner '{folder}' im Icon-Ordner '{icon_folder}' existiert nicht.")

# Beispielaufruf mit einem Basispfad
base_path = r"C:\Users\milan\Documents\Programming\PxC-Projects\icon-repo\Icons\fluentemoji"
delete_folders(base_path)

# Beispielaufruf mit einem Basispfad
# base_path = "C:/Users/milan/Documents/Programming/PxC-Projects/icon-repo/Icons/fluentemoji"
# output_json_path = "C:/Users/milan/Documents/Programming/PxC-Projects/icon-repo/Icons/output.json"
# create_json_from_png_folder(base_path, output_json_path)

# Beispielaufruf mit einem Ordnerpfad
# folder_path = "C:/Users/EMGZ2E/Git-Repositories/icon-repo/Icons/tabler/outline"
# output_json_path = "C:/Users/EMGZ2E/Git-Repositories/icon-repo/Icons/output.json"
# create_json_from_svg_folder(folder_path, output_json_path)