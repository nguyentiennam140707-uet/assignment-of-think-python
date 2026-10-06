class Date:
    def make_date(year, month, day):
        date = Date()
        date.year = year
        date.month = month
        date.day = day
        return date

    def print_date(date):
        print(f'{date.year:04d}, {date.month:04d}, {date.day:04d}')

    def date_to_tuple(date):
        return (date.year, date.month, date.day)
    def is_after(d1, d2):
        return Date.date_to_tuple(d1) > Date.date_to_tuple(d2)
date1 = Date.make_date(1933, 6, 22)
print(date1.year)
print(date1.month)
print(date1.day)

date2 = Date.make_date(2026, 9, 2)
print(Date.is_after(date2, date1))
