
class LenDataError(Exception):
    def __str__(self):
        return 'Неверное количество данных'


class FormatError(Exception):
    def __str__(self):
        return 'Неверный формат записи'


def list_data():
    data_list = []
    rep = ["Введите Ф.И.О", "Введите дату рождения", "Введите номер телефона", "Введите пол"]
    for i in range(len(rep)):
        print(rep[i])
        x = input()
        data_list.append(x)
    return  data_list

res = list_data()

def valid_data(lst):
    if len(lst) != 4:
        raise LenDataError
    fio, date ,phone, gender = lst
    if fio.count('.') != 2:
        raise FormatError

    if date.count('.') != 2:
        raise FormatError

    if not phone.isdigit():
        raise FormatError
    return lst


data = valid_data(res)
famaly, n , s = data[0].split(".")

with open(famaly, 'w') as writer:
    for i in data:
        writer.writelines(i + ' ')






