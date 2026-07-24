import csv
import io
import zipfile
from pathlib import Path
from src.models.csv_analysis import CsvAnalysis


def read_csv_headers(
    zip_path: Path,
    internal_zip_name: str,
    csv_name: str,
) -> tuple[list[str], list[str]]:
    """
    Devuelve el encabezado y la primera fila de un CSV
    contenido dentro de un ZIP interno.
    """

    with zipfile.ZipFile(zip_path, "r") as main_zip:

        with main_zip.open(internal_zip_name) as zip_data:

            zip_bytes = io.BytesIO(zip_data.read())

            with zipfile.ZipFile(zip_bytes) as internal_zip:

                with internal_zip.open(csv_name) as csv_file:

                    text = io.TextIOWrapper(
                        csv_file,
                        encoding="utf-8-sig",
                    )

                    reader = csv.reader(text, delimiter="|")

                    headers = next(reader)
                    first_row = next(reader)

                    return headers, first_row


def analyze_csv(
    zip_path: Path,
    internal_zip_name: str,
    csv_name: str,
) -> dict:
    """
    Analiza un CSV y devuelve información útil.
    """

    with zipfile.ZipFile(zip_path, "r") as main_zip:

        with main_zip.open(internal_zip_name) as zip_data:

            zip_bytes = io.BytesIO(zip_data.read())

            with zipfile.ZipFile(zip_bytes) as internal_zip:

                with internal_zip.open(csv_name) as csv_file:

                    text = io.TextIOWrapper(
                        csv_file,
                        encoding="utf-8-sig",
                    )

                    reader = csv.reader(text, delimiter="|")

                    headers = next(reader)
                    first_row = next(reader)

                    row_count = 1

                    for _ in reader:
                        row_count += 1

                    return CsvAnalysis(
                        headers=headers,
                        first_row=first_row,
                        row_count=row_count,
                    )