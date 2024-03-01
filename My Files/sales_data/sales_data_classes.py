from dataclasses import dataclass


@dataclass
class Sale:
    year: int = 0
    month: int = 0
    day: int = 0
    region: str = ''
    amount: float = 0.0

    @property
    def get_date(self):
        return f'{self.year}-{self.month}-{self.day}'

    def get_quarter(self):
        if self.month in [1, 2, 3]:
            return 1
        elif self.month in [4, 5, 6]:
            return 2
        elif self.month in [7, 8, 9]:
            return 3
        else:
            return 4


@dataclass
class Regions:
    
