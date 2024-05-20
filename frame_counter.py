import ffmpeg
import os

def get_frame_count(video_path):
    probe = ffmpeg.probe(video_path)
    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    return int(video_info['nb_frames'])

def main():
    video_directory = input("Enter the directory path of the video file: ")
    video_name = input("Enter the name of the video file (including extension): ")
    video_path = os.path.join(video_directory, video_name)
    frame_count = get_frame_count(video_path)
    print("Number of frames in the video:", frame_count)

if __name__ == "__main__":
    main()
