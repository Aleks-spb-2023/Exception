


arr1 = [4, 6, 7, 89, 3, 6, 7]
arr2 = [5, 9, 3, 7, 9, 7, 5]

class DifferentLengthError(Exception):
    def __str__(self):
        return ' У массивов не совпадает длина'





def sub_array(arr1, arr2):
        if len(arr1) != len(arr2):
            raise DifferentLengthError

        return list(map(lambda x, y: x - y, arr1, arr2))


def division_array(arr1, arr2):
    if len(arr1) != len(arr2):
        raise RuntimeError('Не совпадает длина массивов')

    return list(map(lambda x, y: x / y, arr1, arr2))


print(sub_array(arr1, arr2))
print(division_array(arr1, arr2))