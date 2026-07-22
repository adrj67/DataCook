from pathlib import Path
import io
import zipfile


def get_internal_zip_files(zip_path: Path) -> list[str]:
    """
    Devuelve la lista de ZIP contenidos en el ZIP principal.
    """

    with zipfile.ZipFile(zip_path, "r") as main_zip:

        return [
            file_name
            for file_name in main_zip.namelist()
            if file_name.endswith(".zip")
        ]


def get_csv_files(zip_path: Path, internal_zip_name: str) -> list[str]:
    """
    Devuelve los CSV contenidos en un ZIP interno.
    """

    with zipfile.ZipFile(zip_path, "r") as main_zip:

        with main_zip.open(internal_zip_name) as zip_data:

            zip_bytes = io.BytesIO(zip_data.read())

            with zipfile.ZipFile(zip_bytes) as internal_zip:

                return internal_zip.namelist()