import os
import subprocess
import sys
import time

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

def apply_ffmpeg_command(directory_path, gpu_vendor, codec, bitrate, fps):
    total_start_time = time.time()  # Время начала выполнения скрипта
    
    if gpu_vendor in ['n', 'nvidia']:
        if codec.lower() == 'h264':
            codec_name = 'h264_nvenc'
        elif codec.lower() == 'h265':
            codec_name = 'hevc_nvenc'
        else:
            print("Неподдерживаемый кодек.")
            return
    elif gpu_vendor in ['a', 'amd']:
        if codec.lower() == 'h264':
            codec_name = 'h264_amf'
        elif codec.lower() == 'h265':
            codec_name = 'hevc_amf'
        else:
            print("Неподдерживаемый кодек.")
            return
    else:
        print("Неподдерживаемый производитель видеокарты.")
        return

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.mp4'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + f'_mod.mp4')
                command = (
                    f'ffmpeg -i "{input_file}" -r {fps} -c:v {codec_name} -b:v {bitrate}k -c:a copy "{output_file}"'
                )
                
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
                new_output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + f'.mp4')
                os.rename(output_file, new_output_file)
    
    total_end_time = time.time()  # Время окончания выполнения скрипта
    total_time = total_end_time - total_start_time
    print(f"{Fore.GREEN}Общее время выполнения скрипта: {total_time:.2f} секунд ({format_time(total_time)}){Style.RESET_ALL}")

if not check_ffmpeg_installed():
    install_ffmpeg()

directory_path = input("Введите путь к директории: ")

while True:
    gpu_vendor = input("Введите производителя видеокарты (n - NVIDIA, a - AMD): ").lower()
    if gpu_vendor in ['n', 'nvidia', 'a', 'amd']:
        break
    else:
        print("Введено неверное значение. Пожалуйста, введите 'n' для NVIDIA или 'a' для AMD.")

while True:
    codec = input("Введите кодек (h264 или h265): ").lower()
    if codec in ['h264', 'h265']:
        break
    else:
        print("Введено неверное значение. Пожалуйста, введите 'h264' или 'h265'.")

bitrate = input("Введите битрейт (в килобитах/сек): ")

while True:
    try:
        fps = int(input("Введите желаемую частоту кадров (FPS): "))
        if fps > 0:
            break
        else:
            print("FPS должно быть положительным числом.")
    except ValueError:
        print("Пожалуйста, введите корректное числовое значение для FPS.")

apply_ffmpeg_command(directory_path, gpu_vendor, codec, bitrate, fps)
