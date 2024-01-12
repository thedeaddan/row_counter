import os
from colorama import Fore, Back, Style, init
from tqdm import tqdm
from tabulate import tabulate

# Инициализация colorama
init(autoreset=True)

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except Exception as e:
        return 0

def count_lines_in_directory(directory):
    total_lines = 0
    file_count = 0
    file_data = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") or file.endswith(".html") or file.endswith(".js") or file.endswith(".py"):
                file_path = os.path.join(root, file)
                lines = count_lines_in_file(file_path)
                total_lines += lines
                file_count += 1
                file_data.append([file_path, lines])

    return total_lines, file_count, file_data

def main():
    current_directory = os.getcwd()
    total_lines, file_count, file_data = count_lines_in_directory(current_directory)

    print(Fore.GREEN + f"Найдено {file_count} файлов с расширением .py")
    print(Fore.GREEN + f"Общее количество строк: {total_lines}\n")

    table_headers = ["Файл", "Количество строк", "Процент от общего"]
    table_data = []

    for data in file_data:
        file_path, lines = data
        percentage = (lines / total_lines) * 100
        table_data.append([file_path, lines, f"{percentage:.2f}%"])

    # Вывод таблицы
    print(tabulate(table_data, headers=table_headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
