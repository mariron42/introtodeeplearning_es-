import os
import subprocess
import time

# Forzar UTF-8
os.environ["PYTHONUTF8"] = "1"

def translate_file(file_path):
    es_path = file_path.replace(".ipynb", "_es.ipynb")
    if os.path.exists(es_path):
        print(f"Saltando (ya existe): {es_path}")
        return

    print(f"Traduciendo: {file_path}")
    # Usamos delay de 20 segundos y reintentos manuales si es necesario
    try:
        result = subprocess.run(
            ["python", "-m", "jupyter_translate", file_path, "--target", "es", "--delay", "20"],
            shell=True
        )
        if result.returncode == 0:
            print(f"OK: {file_path}")
        else:
            print(f"FALLÓ: {file_path}")
    except Exception as e:
        print(f"Error en {file_path}: {e}")

def main():
    workspace_root = os.getcwd()
    folders = ["lab1", "lab2", "lab3"]
    
    to_translate = []
    for folder in folders:
        folder_path = os.path.join(workspace_root, folder)
        if not os.path.exists(folder_path):
            continue
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".ipynb") and not file.endswith("_es.ipynb"):
                    full_path = os.path.join(root, file)
                    es_path = full_path.replace(".ipynb", "_es.ipynb")
                    if not os.path.exists(es_path):
                        to_translate.append(full_path)

    print(f"Archivos pendientes: {len(to_translate)}")
    for f in to_translate:
        translate_file(f)
        # Espera entre archivos para no saturar la API
        print("Esperando 30 segundos antes del siguiente archivo...")
        time.sleep(30)

if __name__ == "__main__":
    main()
