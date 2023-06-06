
#1 Задание
def floatNumber():
    num = input()
    try:
        num = float(num)
        return num
    except:
        print("Введите число")
        return floatNumber()


print(floatNumber())




# 2 Задание
# Ошибка в том что нельзять делить масссив на число тк разные типы данных

d = 0
array = [1, 2, 3, 4, 5, 6, 7, 8]

try:
    catchedRes1 = array / d
    print("catchedRes1 = " + catchedRes1)
except TypeError as tp:
    print('ошибка-->', tp)


# 3 В другом файле ---->





# 4

def StringInput():
    string = input()
    if len(string) == 0:
        raise Exception("Длина строки должна быть больше нуля")

    return string



StringInput()