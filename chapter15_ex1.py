class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.year:04d}, {self.month:02d}, {self.day:02d}'
    def to_tuple(self):
        return (self.year, self.month, self.day)
    def is_after(self, other):
        return self.to_tuple() > other.to_tuple()

date1 = Date(1933, 6, 22)
print(date1.__str__())
date2 = Date(1933, 11, 17)
print(date2.is_after(date1))

