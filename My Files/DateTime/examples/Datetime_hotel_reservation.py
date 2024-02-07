from datetime import datetime


def title():
    print("The Hotel Reservation program\n")


def arrival():
    a_date = input("Enter the arrival date (YYYY-MM-DD): ")
    a_date = datetime.strptime(a_date, "%Y-%m-%d")
    return a_date


def departure():
    d_date = input("Enter the departure date (YYYY-MM-DD): ")
    d_date = datetime.strptime(d_date, "%Y-%m-%d")
    print()
    return d_date


def total_nights(a_date, d_date):
    nights = d_date - a_date
    return nights


def total_price(nights, rate):
    price = nights * rate
    return price


def get_rate(a_date):
    month = a_date.month
    if month in [6, 7, 8]:
        rate = 105.00
    else:
        rate = 85.00
    return rate


def main():
    title()
    while True:
        a_date = arrival()
        d_date = departure()
        nights = total_nights(a_date, d_date).days
        rate = get_rate(a_date)
        price = total_price(nights, rate)
        print(f"Arrival Date:\t{a_date: %B %d, %Y}")
        print(f"Departure Date: {d_date: %B %d, %Y}")
        if rate == 105:
            print(f"Nightly rate:\t ${rate:.2f} (High season)")
        else:
            print(f"Nightly rate:\t ${rate:.2f}")
        print(f"Total nights:\t {nights}")
        print(f"Total price:\t ${price:.2f}\n")

        user_input = input("Do you want to continue? (y/n): ").lower()
        print()
        if user_input == 'n':
            print('Bye!')
            break


main()
