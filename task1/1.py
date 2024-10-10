import sys


def circular_array_path(n, m):

    circular_array = list(range(1, n + 1))
    path = []


    current_index = 0

    while True:

        start_element = circular_array[current_index]
        path.append(start_element)


        current_index = (current_index + m) % n


        if current_index == 0:
            break

    return ''.join(map(str, path))


if __name__ == "__main__":
    # Получаем аргументы командной строки
    if len(sys.argv) != 3:
        print("Usage: python script.py n m")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    # Вызываем функцию и печатаем результат
    result = circular_array_path(n, m)
    print(result)