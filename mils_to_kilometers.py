import osa

def average():
    path = input('Введите путь к файлу: ')
    length = []
    with open(path, 'r') as length_file:
        for line_length in length_file:
            line = line_length.split(' ')
            length.append(float(line[1].replace(',','')))
    return sum(length)

def convert_temp(length):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    return client.service.ChangeLengthUnit(length,'Miles','Kilometers')


if __name__=='__main__':

    print('Путь в километрах составил: {} км'.format(round(convert_temp(average()),2)))