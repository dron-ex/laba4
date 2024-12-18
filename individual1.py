if __name__ == '__main__':
    s1 = input("Введите слово s1: ")
    s2 = ''.join(s1[i] for i in range(len(s1)) if i % 2 == 0)  # Берем буквы с четными индексами
    print(f'Слово s2 из нечетных букв слова s1: {s2}')