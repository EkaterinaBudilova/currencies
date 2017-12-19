import osa

def average():
    path = input('Введите путь к файлу: ')
    temps = []
    with open(path, 'r') as temps_file:
        for file_line in temps_file:
            line = file_line.split(' ')
            temps.append(int(line[0]))
    return sum(temps) / len(temps)

def convert_temp(temp):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(temp,'degreeFahrenheit','degreeCelsius')


if __name__=='__main__':

    average_temp = average()
    print('Средняя температура в градусах по Фаренгейту: {}'.format(average_temp))
    print('Средняя температура в градусах по Цельсию: {}'.format(convert_temp(average_temp)))