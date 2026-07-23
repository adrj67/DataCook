from pathlib import Path

from src.zip_explorer import (
    get_internal_zip_files,
    get_csv_files,
)

from src.csv_explorer import read_csv_headers

from src.csv_explorer import analyze_csv


ZIP_FILE = Path(
    r"C:\Users\adrj\Escritorio\Argentina Programa\Flutter\App_DataCook\sepa_viernes.zip"
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

    print("\n-----------------------------------")
    print("Analizando productos.csv")
    print("-----------------------------------")

    analysis = analyze_csv(
        ZIP_FILE,
        first_zip,
        "productos.csv",
    )

    print(f"\nFilas: {analysis['row_count']}")
    print(f"Columnas: {len(analysis['headers'])}")

    print("\nColumnas:\n")

    for column in analysis["headers"]:
        print(f"- {column}")

    print("\nPrimer registro:\n")

    for column, value in zip(
        analysis["headers"],
        analysis["first_row"],
    ):
        print(f"{column}: {value}")


if __name__ == "__main__":
    main()