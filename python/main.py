from pathlib import Path

from src.zip_explorer import explore_zip

# Ruta del archivo ZIP a procesar
ZIP_FILE = Path(
    r""
)


def main():
    print("===================================")
    print("       DataCook iniciado")
    print("===================================")

    explore_zip(ZIP_FILE)


if __name__ == "__main__":
    main()