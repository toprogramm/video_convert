import os
from colorama import Fore, Style

def apply_ffmpeg_command(directory_path):
    directory_path = directory_path.replace("\\", "\\")  # Заменяем обратные слеши на прямые
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.mp4'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '_mod.mp4')
                command = f'ffmpeg -i "{input_file}" -c:v libaom-av1 -b:v 1500k -c:a copy "{output_file}"'
                os.system(command)
                input_size = os.path.getsize(input_file)
                output_size = os.path.getsize(output_file)
                print(f"{Fore.RED}Исходный файл: {input_file}, Размер: {int(input_size / 1048576)} мбайт{Style.RESET_ALL}")
                print(f"{Fore.RED}Конечный файл: {output_file}, Размер: {int(output_size / 1048576)} мбайт{Style.RESET_ALL}")
                os.remove(input_file)  # Удаление исходного файла после конвертации
                # Переименование выходного файла без суффикса "_mod"
                new_output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '.mp4')
                os.rename(output_file, new_output_file)

directory_path = input("Введите путь к директории: ")
apply_ffmpeg_command(directory_path)
