def caesar_encrypt(text, shift):
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
        else:
            result += char
    return result

text = input('Введите строку (буквами русского алфавита): ')
shift = int(input('Введите отступ (число): '))
print(caesar_encrypt(text,shift))