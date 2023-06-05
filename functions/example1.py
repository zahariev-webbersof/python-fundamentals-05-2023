# Работи 
from forex_python.converter import CurrencyRates

def get_exchange_rate(base_currency, target_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(base_currency, target_currency)
    return exchange_rate

def convert_currency(base_currency, target_currency, amount):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    convert_amount = amount * exchange_rate
    return convert_amount

if __name__ == '__main__':
    base_currency = input('Enter a base currency: ')
    target_currency = input('Enter a target currency: ')
    amount = int(input('Currency amount: '))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    convert_amount = convert_currency(base_currency, target_currency, amount)

    print(f'Exchange rate: 1 {base_currency} = {exchange_rate:.2f} {target_currency}')
    print(f'{amount} {base_currency} = {convert_amount}')