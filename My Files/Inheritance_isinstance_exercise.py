from dataclasses import dataclass


@dataclass
class Product:
    name: str = ''
    discount_price: float = 0.0

    def getDiscountAmount(self) -> str:
        return f"Discount price:\t{self.discount_price}"

    def getName(self) -> str:
        return f"Name:\t\t\t{self.name}"


@dataclass
class Movie(Product):
    year: int = 0

    def getYear(self):
        return f"Year:\t\t\t{self.year}"


def main():
    product = Product("Stanley 13 Ounce Wood Hammer", 4.94)
    print("PRODUCT DATA")
    print(product.getName())
    print(product.getDiscountAmount())

    movie = Movie("The Holy Grail - DVD", 4.80, 1975)
    print("\nPRODUCT DATA")
    print(movie.getName())
    print(movie.getYear())
    print(movie.getDiscountAmount())


if __name__ == "__main__":
    main()
