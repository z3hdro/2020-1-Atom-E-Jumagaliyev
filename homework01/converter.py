class Currency:
    currencies = ['RUB', 'KZT', 'USD', 'EUR', 'CNY']
    currency_values = {
        ('RUB', 'KZT'): 0.19,
        ('RUB', 'USD'): 74.03,
        ('RUB', 'EUR'): 83.66,
        ('RUB', 'CNY'): 10.59,
        ('KZT', 'RUB'): 5.40,
        ('KZT', 'USD'): 406.55,
        ('KZT', 'EUR'): 450.15,
        ('KZT', 'CNY'): 57.83,
        ('USD', 'RUB'): 0.014,
        ('USD', 'EUR'): 1.11,
        ('USD', 'KZT'): 0.0025,
        ('EUR', 'RUB'): 0.012,
        ('EUR', 'CNY'): 0.13,
        ('EUR', 'KZT'): 0.0022,
        ('EUR', 'USD'): 0.90,
        ('CNY', 'RUB'): 0.09,
        ('CNY', 'EUR'): 7.78,
        ('CNY', 'KZT'): 0.017,
        ('CNY', 'USD'): 7.03
    }

    def __init__(self, num, cur='RUB'):
        if cur in self.currencies:
            self.num = num
            self.cur = cur
        else:
            raise AttributeError('Wrong currency')

    def __repr__(self):
        return 'Value: {value}, Currency: {curr}'.format(
            value=self.num, curr=self.cur)

    def __str__(self):
        return '{value} {currency}'.format(value=self.num, currency=self.cur)

    @property
    def value(self):
        return self.num

    @property
    def currency(self):
        return self.cur

    @currency.setter
    def currency(self, currency):
        if currency != self.cur:
            if currency in self.currencies:
                self.num = self.num * self.currency_values.get(
                    (currency, self.cur))
                self.cur = currency
            else:
                raise ValueError('Such currency does not supported!')

    def __add__(self, other):
        if type(other) in [int, float]:
            return Currency(self.num + other, self.cur)
        if type(other) is Currency:
            coef = self.currency_values.get((self.cur, other.cur))
            return Currency(self.num + other.num * coef, self.cur)
        else:
            raise ValueError('Wrong Addition')
