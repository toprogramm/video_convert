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
        print("FFmpeg not found. Installing FFmpeg...")
        os.system("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
        os.system("choco upgrade ffmpeg")
    else:  # Linux / MacOS
        print("FFmpeg not found. Installing FFmpeg...")
        os.system("sudo apt-get update && sudo apt-get install -y ffmpeg")

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return f"{int(hours)}h:{int(mins)}m:{int(secs)}s"

def apply_ffmpeg_command(directory_path, gpu_vendor, codec, bitrate):
    total_start_time = time.time()  # Start time of the script execution
    
    if gpu_vendor in ['n', 'nvidia']:
        if codec.lower() == 'h264':
            codec_name = 'h264_nvenc'
        elif codec.lower() == 'h265':
            codec_name = 'hevc_nvenc'
        else:
            print("Unsupported codec.")
            return
    elif gpu_vendor in ['a', 'amd']:
        if codec.lower() == 'h264':
            codec_name = 'h264_amf'
        elif codec.lower() == 'h265':
            codec_name = 'hevc_amf'
        else:
            print("Unsupported codec.")
            return
    else:
        print("Unsupported GPU vendor.")
        return

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.mp4'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + f'_mod.mp4')
                command = f'ffmpeg -i "{input_file}" -c:v {codec_name} -b:v {bitrate}k -c:a copy "{output_file}"'
                
                start_time = time.time()  # Start time of file encoding
                os.system(command)
                end_time = time.time()  # End time of file encoding
                
                input_size = os.path.getsize(input_file)
                output_size = os.path.getsize(output_file)
                
                file_time = end_time - start_time
                print(f"{Fore.RED}Input file: {input_file}, Size: {int(input_size / 1048576)} MB{Style.RESET_ALL}")
                print(f"{Fore.RED}Output file: {output_file}, Size: {int(output_size / 1048576)} MB{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}File encoding time: {file_time:.2f} seconds ({format_time(file_time)}){Style.RESET_ALL}")
                
                os.remove(input_file)  # Removing the input file after conversion
                # Renaming the output file without the "_mod" suffix
                new_output_file = os.path.join(root, '.'.join(file.split('.')[:-1]) + f'.mp4')
                os.rename(output_file, new_output_file)
    
    total_end_time = time.time()  # End time of the script execution
    total_time = total_end_time - total_start_time
    print(f"{Fore.GREEN}Total script execution time: {total_time:.2f} seconds ({format_time(total_time)}){Style.RESET_ALL}")

if not check_ffmpeg_installed():
    install_ffmpeg()

directory_path = input("Enter the directory path: ")

while True:
    gpu_vendor = input("Enter the GPU vendor (n - NVIDIA, a - AMD): ").lower()
    if gpu_vendor in ['n', 'nvidia', 'a', 'amd']:
        break
    else:
        print("Incorrect value entered. Please enter 'n' for NVIDIA or 'a' for AMD.")

while True:
    codec = input("Enter the codec (h264 or h265): ").lower()
    if codec in ['h264', 'h265']:
        break
    else:
        print("Incorrect value entered. Please enter 'h264' or 'h265'.")

bitrate = input("Enter the bitrate (in kilobits/second): ")

apply_ffmpeg_command(directory_path, gpu_vendor, codec, bitrate)
