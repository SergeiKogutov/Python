import json
import os

def merge_json_files(input_directory, output_file):
    merged_data = {}

    # Проходим по всем файлам в указанной директории
    for index, filename in enumerate(os.listdir(input_directory), start=1):
        if filename.endswith('.json'):
            file_path = os.path.join(input_directory, filename)
            with open(file_path, 'r', encoding='utf-8') as json_file:
                try:
                    data = json.load(json_file)
                    merged_data[f'parse_{index}'] = data  # Нумеруем файлы
                except json.JSONDecodeError as e:
                    print(f"Ошибка при чтении файла {filename}: {e}")

    # Записываем объединенные данные в новый JSON файл
    with open(output_file, 'w', encoding='utf-8') as output_json_file:
        json.dump(merged_data, output_json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_directory = 'resultdata'  # Укажите путь к директории с JSON файлами
    output_file = 'merged_output.json'  # Укажите имя выходного файла
    merge_json_files(input_directory, output_file)
    print(f"Объединенные данные записаны в {output_file}")