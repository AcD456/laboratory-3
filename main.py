from date import find_dates_in_text, read_file, fetch_url_content
import requests

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
            file_path = input("Введите путь к файлу: ").strip()
            try:
                text = read_file(file_path)
            except FileNotFoundError:
                print(f"Файл {file_path} не найден.")
                continue
            dates = find_dates_in_text(text)
            if dates:
                print("Найденные корректные даты:")
                for date in dates:
                    print(date)
            else:
                print("Корректные даты не найдены.")

        elif choice == "3":
            url = input("Введите URL: ").strip()
            try:
                text = fetch_url_content(url)
            except requests.RequestException as e:
                print(f"Ошибка при загрузке URL: {e}")
                continue

            dates = find_dates_in_text(text)
            if dates:
                print("Найденные корректные даты:")
                for date in dates:
                    print(date)
            else:
                print("Корректные даты не найдены.")

        elif choice == "0":
            print("Завершение работы программы.")
            return 0

main_menu()