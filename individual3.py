def remove_letters_s(text):
    # Удаляем буквы 'с' и 'c'
    result = text.replace('с', '').replace('С', '').replace('c', '').replace('C', '')
    return result


if __name__ == '__main__':
    # Считываем предложение от пользователя
    sentence = input("Введите предложение: ")

    # Удаляем буквы 'с' и 'c'
    modified_sentence = remove_letters_s(sentence)

    print("Измененное предложение:", modified_sentence)