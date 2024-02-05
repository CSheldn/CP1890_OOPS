from datetime import datetime, timedelta


def title():
    print('The Invoice Due Date program\n')


def get_date():
    while True:
        invoice_date = input('Enter the invoice date (MM/DD/YY): ')
        print()
        if invoice_date.strip('/').isnumeric() or invoice_date.count('/') != 2:
            print('Invalid date. Try again.')
        else:
            invoice_date = datetime.strptime(invoice_date, '%m/%d/%y')
            return invoice_date


def get_due_date(invoice_date):
    due_date = invoice_date + timedelta(days=30)
    return due_date


def time_left(current_date, due_date):
    days_left = current_date - due_date
    if days_left.days < 0:
        print('You have ' + str(days_left.days) + ' days')
    elif days_left.days == 0:
        print('This invoice is due today !')
    else:
        print('This invoice is ' + str(days_left.days) + ' day(s) overdue.')


def main():
    title()
    while True:
        invoice = get_date()
        due = get_due_date(invoice)
        current_date = datetime.now()
        print(f'Invoice Due date:{invoice: %B %d, %Y}')
        print(f'Due date:{due: %B %d, %Y}')
        print(f'Current date:{current_date: %B %d, %Y}\n')
        time_left(current_date, due)
        print()

        user_input = input('Do you want to continue? (y/n): ')
        if user_input.lower() == 'n':
            break


if __name__ == '__main__':
    main()
