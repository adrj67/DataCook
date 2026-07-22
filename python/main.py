from pathlib import Path

from src.zip_explorer import (
    get_internal_zip_files,
    get_csv_files,
)

ZIP_FILE = Path(
    r""
)


def main():
    print("===================================")
    print("       DataCook iniciado")
    print("===================================")

    zip_files = get_internal_zip_files(ZIP_FILE)

    print(f"\nZIP encontrados: {len(zip_files)}\n")

    for index, file_name in enumerate(zip_files, start=1):
        print(f"{index:2}. {file_name}")

    first_zip = zip_files[0]

    print("\n-----------------------------------")
    print(f"Primer ZIP: {first_zip}")
    print("-----------------------------------\n")

    csv_files = get_csv_files(ZIP_FILE, first_zip)

    print("Contenido:")

    for csv in csv_files:
        print(f" - {csv}")


if __name__ == "__main__":
    main()