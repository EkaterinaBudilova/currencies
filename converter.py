import osa

def converter(money, mony_type):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum(fromCurrency=mony_type, toCurrency='RUB', amount=money , rounding=True)

def average():
    path = input('Введите путь к файлу: ')
    money = []
    with open(path, 'r') as temps_file:
        for file_line in temps_file:
            line = file_line.split(' ')
            money.append(converter(float(line[1]), line[2].strip()))
    return round(sum(money))


if __name__=='__main__':

    print('Сумма затрат составит: {} рублей.'.format(average()))
