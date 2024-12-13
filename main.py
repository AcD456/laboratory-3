from date import find_dates_in_text

def main_menu():
    while True:
        print("\nВыберите, откуда взять даты на проверку:")
        print("1. Ввод с клавиатуры.")
        print("2. Из файла.")
        print("3. Найти даты на сайте.")
        print("0. Завершение работы программы.")

        choice = input("Введите номер варианта: ")

        if choice == "1":
            text = input("Введите текст для поиска дат: ")
            dates = find_dates_in_text(text)
            print("Найденные корректные даты:", dates)



        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "0":
            print("Завершение работы программы.")
            return 0

main_menu()