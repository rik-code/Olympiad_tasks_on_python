first_lst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
       'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
second_lst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
        'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


def encryptCaesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in first_lst:
            ind = first_lst.index(x)
            ret += first_lst[ind+shift]
        elif x in second_lst:
            ind = second_lst.index(x)
            ret += second_lst[ind+shift]
        else:
            ret += x
    return ret


def decryptCaesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in first_lst:
            ind = first_lst.index(x)
            ret += first_lst[ind-shift]
        elif x in second_lst:
            ind = second_lst.index(x)
            ret += second_lst[ind-shift]
        else:
            ret += x
    return ret

