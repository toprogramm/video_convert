import subprocess

def change_fps(input_file: str, output_file: str, fps: int):

    try:
        # Команда для изменения FPS
        command = [
            "ffmpeg",
            "-i", input_file,         # Входной файл
            "-r", str(fps),           # Новая частота кадров
            output_file               # Выходной файл
        ]
        
        # Выполняем команду
        subprocess.run(command, check=True)
        print(f"FPS видео изменён на {fps}. Результат сохранён в '{output_file}'")
    except subprocess.CalledProcessError as e:
        print("Ошибка при выполнении команды FFmpeg:", e)
    except FileNotFoundError:
        print("FFmpeg не установлен или не найден в PATH.")

# Пример использования
input_video = "input.mp4"  # Укажите путь к вашему видеофайлу
output_video = "output.mp4"  # Укажите путь к выходному видеофайлу
new_fps = 30  # Новая частота кадров

change_fps(input_video, output_video, new_fps)
