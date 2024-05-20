import os
import subprocess
import sys
import time

# Проверка наличия colorama и установка, если отсутствует
try:
    from colorama import Fore, Style
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import Fore, Style

def check_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_ffmpeg():
    if os.name == "nt":  # Windows
        print("FFmpeg не найден. Установка FFmpeg...")
        os.system("choco install ffmpeg")
    else:  # Linux / MacOS
        print("FFmpeg не найден. Установка FFmpeg...")
        os.system("sudo apt-get update && sudo apt-get install -y ffmpeg")

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return f"{int(hours)}ч:{int(mins)}м:{int(secs)}с"

def apply_ffmpeg_command(directory_path):
    total_start_time = time.time()  # Время начала выполнения скрипта

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.mp4'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '_mod.mp4')
                command = f'ffmpeg -i "{input_file}" -c:v hevc_nvenc -b:v 1500k -c:a copy "{output_file}"'
                
                start_time = time.time()  # Время начала кодирования файла
                os.system(command)
                end_time = time.time()  # Время окончания кодирования файла
                
                input_size = os.path.getsize(input_file)
                output_size = os.path.getsize(output_file)
                
                file_time = end_time - start_time
                print(f"{Fore.RED}Исходный файл: {input_file}, Размер: {int(input_size / 1048576)} мбайт{Style.RESET_ALL}")
                print(f"{Fore.RED}Конечный файл: {output_file}, Размер: {int(output_size / 1048576)} мбайт{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Время кодирования файла: {file_time:.2f} секунд ({format_time(file_time)}){Style.RESET_ALL}")
                
                os.remove(input_file)  # Удаление исходного файла после конвертации
                # Переименование выходного файла без суффикса "_mod"
                new_output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + '.mp4')
                os.rename(output_file, new_output_file)
    
    total_end_time = time.time()  # Время окончания выполнения скрипта
    total_time = total_end_time - total_start_time
    print(f"{Fore.GREEN}Общее время выполнения скрипта: {total_time:.2f} секунд ({format_time(total_time)}){Style.RESET_ALL}")

if not check_ffmpeg_installed():
    install_ffmpeg()

directory_path = input("Введите путь к директории: ")
apply_ffmpeg_command(directory_path)
