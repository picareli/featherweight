from dataclasses import dataclass
from datetime import date
from typing import NamedTuple


class Entry(NamedTuple):
    date_added: date
    value: float


@dataclass
class Profile:
    height: float
    target_weight: float
    target_date: date
    bmi: float
    max_weight: float
    min_weight: float
    entries: Entry

    def calculate_bmi(self, height: float, weight: float):
        return height / (weight**2)
