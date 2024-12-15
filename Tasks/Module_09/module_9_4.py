# Домашнее задание по теме "Создание функций на лету"

from random import choice


def get_advanced_writer(file_name: str):
    def write_everything(*data_set):
        with open(file_name, "a") as file:
            for data in data_set:
                file.write(f"{str(data)}\n")

    return write_everything


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


if __name__ == "__main__":
    # Lambda-функция
    first = "Мама мыла раму"
    second = "Рамена мало было"
    print(list(map(lambda char_1, char_2: char_1 == char_2, first, second)))

    # Замыкание
    write = get_advanced_writer("example.txt")
    write("Это строчка", ["А", "это", "уже", "число", 5, "в", "списке"])

    # Метод __call__
    first_ball = MysticBall("Да", "Нет", "Наверное")
    print(first_ball())
    print(first_ball())
    print(first_ball())
