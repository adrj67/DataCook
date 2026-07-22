from pathlib import Path
import zipfile


def explore_zip(zip_path: Path):
    print("\nArchivo seleccionado:\n")

    if not zip_path.exists():
        print(f"No existe el archivo:\n{zip_path}")
        return

    print(f"Nombre : {zip_path.name}")
    print(f"Ruta   : {zip_path}")

    print("\nAbriendo archivo ZIP...\n")

    try:
        with zipfile.ZipFile(zip_path, "r") as zip_file:

            # file_list = zip_file.namelist()

            # print(f"Cantidad de archivos: {len(file_list)}\n")

            # for index, file_name in enumerate(file_list, start=1):
            #     print(f"{index:2}. {file_name}")

            file_list = zip_file.namelist()

            zip_files = []

            for file_name in file_list:
                if file_name.endswith(".zip"):
                    zip_files.append(file_name)

            print(f"Entradas totales : {len(file_list)}")
            print(f"ZIP encontrados  : {len(zip_files)}\n")

            for index, file_name in enumerate(zip_files, start=1):
                print(f"{index:2}. {file_name}")

    except zipfile.BadZipFile:
        print("El archivo no es un ZIP válido.")