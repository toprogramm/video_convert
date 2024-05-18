# import os

# def apply_ffmpeg_command(directory_path):
#     directory_path = directory_path.replace("\\", "/")  # Заменяем обратные слеши на прямые
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             if file.endswith('.mp4'):
#                 input_file = os.path.join(root, file)
#                 output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '_mod.mp4')
#                 command = f'ffmpeg -i "{input_file}" -c:v h264_amf "{output_file}"'
#                 os.system(command)
#                 input_size = os.path.getsize(input_file)
#                 output_size = os.path.getsize(output_file)
#                 print(f"Исходный файл: {input_file}, Размер: {input_size} байт")
#                 print(f"Конечный файл: {output_file}, Размер: {output_size} байт")

# directory_path = input("Введите путь к директории: ")
# apply_ffmpeg_command(directory_path)


# import os

# def apply_ffmpeg_command(directory_path):
#     directory_path = directory_path.replace("\\", "/")  # Заменяем обратные слеши на прямые
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             if file.endswith('.mp4'):
#                 input_file = os.path.join(root, file)
#                 output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '_mod.mp4')
#                 command = f'ffmpeg -i "{input_file}" -c:v h264_amf "{output_file}"'
#                 os.system(command)
#                 input_size = os.path.getsize(input_file)
#                 output_size = os.path.getsize(output_file)
#                 print(f"Исходный файл: {input_file}, Размер: {input_size} байт")
#                 print(f"Конечный файл: {output_file}, Размер: {output_size} байт")
#                 os.remove(input_file)  # Удаление исходного файла после конвертации

# directory_path = input("Введите путь к директории: ")
# apply_ffmpeg_command(directory_path)

# ------------------------------------------------

# import os

# def apply_ffmpeg_command(directory_path):
#     directory_path = directory_path.replace("\\", "/")  # Заменяем обратные слеши на прямые
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             if file.endswith('.mp4'):
#                 input_file = os.path.join(root, file)
#                 output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '_mod.mp4')
#                 command = f'ffmpeg -i "{input_file}" -c:v h264_amf "{output_file}"'
#                 os.system(command)
#                 input_size = os.path.getsize(input_file)
#                 output_size = os.path.getsize(output_file)
#                 print(f"Исходный файл: {input_file}, Размер: {input_size} байт")
#                 print(f"Конечный файл: {output_file}, Размер: {output_size} байт")
#                 os.remove(input_file)  # Удаление исходного файла после конвертации
#                 # Переименование выходного файла без суффикса "_mod" и добавление случайного числа
                
#                 new_output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '.mp4')
#                 os.rename(output_file, new_output_file)

# directory_path = input("Введите путь к директории: ")
# apply_ffmpeg_command(directory_path)
# -------------------------------------------------------
# import os
# from colorama import Fore, Style

# def apply_ffmpeg_command(directory_path):
#     directory_path = directory_path.replace("\\", "/")  # Заменяем обратные слеши на прямые
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             if file.endswith('.mp4'):
#                 input_file = os.path.join(root, file)
#                 output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '_mod.mp4')
#                 command = f'ffmpeg -i "{input_file}" -c:v h264_amf "{output_file}"'
#                 os.system(command)
#                 input_size = os.path.getsize(input_file)
#                 output_size = os.path.getsize(output_file)
#                 print(f"{Fore.RED}Исходный файл: {input_file}, Размер: {int(input_size / 1048576)} мбайт{Style.RESET_ALL}")
#                 print(f"{Fore.RED}Конечный файл: {output_file}, Размер: {int(output_size / 1048576)} мбайт{Style.RESET_ALL}")
#                 os.remove(input_file)  # Удаление исходного файла после конвертации
#                 # Переименование выходного файла без суффикса "_mod" и добавление случайного числа
#                 new_output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '.mp4')
#                 os.rename(output_file, new_output_file)

# directory_path = input("Введите путь к директории: ")
# apply_ffmpeg_command(directory_path)

# # -------
# import os
# import subprocess
# from colorama import Fore, Style

# def apply_ffmpeg_command(directory_path):
#     directory_path = directory_path.replace("\\", "/")  # Заменяем обратные слеши на прямые
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             if file.endswith('.mp4'):
#                 input_file = os.path.join(root, file)
#                 output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '_mod.mp4')
#                 command = f'ffmpeg -i "{input_file}" -c:v h264_amf "{output_file}"'
#                 # Определяем команду в зависимости от операционной системы
#                 if os.name == 'nt':  # Для Windows
#                     command = f'start powershell.exe -NoExit -Command "{command}"'
#                 else:  # Для других операционных систем
#                     command = f'x-terminal-emulator -e "{command}"'
#                 process = subprocess.Popen(command, shell=True)
#                 process.wait()  # Дожидаемся завершения процесса ffmpeg
#                 input_size = os.path.getsize(input_file)
#                 output_size = os.path.getsize(output_file)
#                 print(f"{Fore.RED}Исходный файл: {input_file}, Размер: {input_size / 1024} кбайт{Style.RESET_ALL}")
#                 print(f"{Fore.RED}Конечный файл: {output_file}, Размер: {output_size / 1024} кбайт{Style.RESET_ALL}")
#                 os.remove(input_file)  # Удаление исходного файла после конвертации
#                 # Переименование выходного файла без суффикса "_mod" и добавление случайного числа
#                 new_output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '.mp4')
#                 os.rename(output_file, new_output_file)

# directory_path = input("Введите путь к директории: ")
# apply_ffmpeg_command(directory_path)
# import os
# import subprocess
# import shlex
# from colorama import Fore, Style

# def apply_ffmpeg_command(directory_path):
#     directory_path = directory_path.replace("\\", "\\")  # Заменяем обратные слеши на двойные
#     directory_path = directory_path.replace("/", "\\")  # Заменяем прямые слеши на двойные
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             if file.endswith('.mp4'):
#                 input_file = os.path.join(root, file)
#                 output_file = os.path.join(root, os.path.splitext(file)[0] + '_mod.mp4')
#                 input_file = f'"{input_file}"' # Заменяем обратные слеши на двойные
#                 output_file = f'"{output_file}"'  # Оборачиваем путь к выходному файлу в кавычки
#                 command = f'ffmpeg -i  {f"{input_file}"} -c:v h264_amf {f"{output_file}"}'
#                 # Определяем команду в зависимости от операционной системы
#                 if os.name == 'nt':  # Для Windows
#                     command = f'start powershell.exe -NoExit -Command & {command}'
#                     print(command)
#                 else:  # Для других операционных систем
#                     command = f'x-terminal-emulator -e "{command}"'
#                 process = subprocess.Popen(shlex.split(command), shell=True)
#                 process.wait()  # Дожидаемся завершения процесса ffmpeg
#                 input_size = os.path.getsize(input_file)
#                 output_size = os.path.getsize(output_file)
#                 print(f"{Fore.RED}Исходный файл: {input_file}, Размер: {input_size / 1024} кбайт{Style.RESET_ALL}")
#                 print(f"{Fore.RED}Конечный файл: {output_file}, Размер: {output_size / 1024} кбайт{Style.RESET_ALL}")
#                 os.remove(input_file)  # Удаление исходного файла после конвертации

# directory_path = input("Введите путь к директории: ")
# apply_ffmpeg_command(directory_path)

import os
from colorama import Fore, Style

def apply_ffmpeg_command(directory_path):
    directory_path = directory_path.replace("\\", "\\")  # Заменяем обратные слеши на прямые
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.mp4'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '_mod.mp4')
                command = f'ffmpeg -i "{input_file}" -c:v h264_amf -b:v 1500k -c:a copy "{output_file}"'
                os.system(command)
                input_size = os.path.getsize(input_file)
                output_size = os.path.getsize(output_file)
                print(f"{Fore.RED}Исходный файл: {input_file}, Размер: {int(input_size / 1048576)} мбайт{Style.RESET_ALL}")
                print(f"{Fore.RED}Конечный файл: {output_file}, Размер: {int(output_size / 1048576)} мбайт{Style.RESET_ALL}")
                os.remove(input_file)  # Удаление исходного файла после конвертации
                # Переименование выходного файла без суффикса "_mod" и добавление случайного числа
                new_output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '.mp4')
                os.rename(output_file, new_output_file)

directory_path = input("Введите путь к директории: ")
apply_ffmpeg_command(directory_path)