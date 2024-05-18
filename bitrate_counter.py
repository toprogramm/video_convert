import os
import ffmpeg

def get_video_bitrate(video_path):
    probe = ffmpeg.probe(video_path)
    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    return int(video_info['bit_rate'])

def analyze_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.mp4') or file_path.endswith('.avi') or file_path.endswith('.mkv'):
                try:
                    bitrate = get_video_bitrate(file_path)
                    if bitrate > 2600000:  # Проверка битрейта (> 2600 kbps)
                        print(f"Video file: {file_path}, Bitrate: {int(bitrate / 1000)} kbps")
                except Exception as e:
                    print(f"Error analyzing {file_path}: {str(e)}")

directory_path = "C:/path/to/file/file.mp4"
