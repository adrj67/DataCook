from dataclasses import dataclass


@dataclass
class CsvAnalysis:
    headers: list[str]
    first_row: list[str]
    row_count: int