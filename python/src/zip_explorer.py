from pathlib import Path


def explore_zip(zip_path: Path):
    print("\nArchivo seleccionado:\n")

    if not zip_path.exists():
        print(f"No existe el archivo:\n{zip_path}")
        return

    print(f"Nombre : {zip_path.name}")
    print(f"Ruta   : {zip_path}")