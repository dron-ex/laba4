def count_letters_in_first_sentence(text):
    # Найдем первое предложение в тексте
    end_of_sentence = text.find('.')

    # Если предложение не найдено, рассмотрим весь текст
    first_sentence = text[:end_of_sentence] if end_of_sentence != -1 else text

    # Подсчитываем количество букв в первом предложении
    letter_count = sum(1 for char in first_sentence if char.isalpha())

    return letter_count


if __name__ == '__main__':
    text = input("Введите текст: ")

    letter_count = count_letters_in_first_sentence(text)

    if letter_count > 0:
        print(f"Количество букв в первом предложении: {letter_count}")
    else:
        print("В первом предложении нет букв.")