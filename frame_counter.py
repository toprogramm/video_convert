import ffmpeg

def get_frame_count(video_path):
    probe = ffmpeg.probe(video_path)
    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    return int(video_info['nb_frames'])

video_path = "C:/path/to/file/file.mp4"
frame_count = get_frame_count(video_path)
print("Количество кадров в видео:", frame_count)
