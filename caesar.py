def caesar_encrypt(text, shift):
    alphabet_lover_eng = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lover = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''

    for char in text:
        if char in alphabet_lover:
            index = (alphabet_lover.index(char) + shift) % len(alphabet_lover)
            result += alphabet_lover[index]
        elif char in alphabet_upper:
            index = (alphabet_upper.index(char) + shift) % len(alphabet_upper)
            result += alphabet_upper[index]
        elif char in alphabet_lover_eng:
            index = (alphabet_lover_eng.index(char) + shift) % len(alphabet_lover_eng)
            result += alphabet_lover_eng[index]
        elif char in alphabet_upper_eng:
            index = (alphabet_upper_eng.index(char) + shift) % len(alphabet_upper_eng)
            result += alphabet_upper_eng[index]
        else:
            result += char
    return result

text = input('Введите строку (русскими или английскими буквами): ')
while True:
    try:
        shift = int(input('Введите отступ (число): '))
        print(caesar_encrypt(text, shift))
        break
    except ValueError:
        print('Отступом должно быть целое число, попробуйте еще раз.')

