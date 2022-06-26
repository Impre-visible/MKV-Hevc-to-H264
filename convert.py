import os
from videoprops import get_video_properties, get_audio_properties

start_dir = r"G:\Films-Séries-Émissions\Films"
movies = os.listdir(start_dir)
MoviesToConvert = []
for movie in movies:
    try:
        movieVideoStats = get_video_properties(f"{start_dir}\\{movie}")
        movieAudioStats = get_audio_properties(f"{start_dir}\\{movie}")
        if os.path.isfile(f"{start_dir}\\{movie}"):
            if ((movieVideoStats['codec_name'] != "h264") or (movieVideoStats['codec_name'] == "h264" and movieAudioStats['codec_name'] != "aac")) and movie.endswith("mkv")):
                MoviesToConvert.append(movie)
                print(movieVideoStats['codec_name'], movieAudioStats['codec_name'], movie)
    except:
        print(f"Problems with {movie}")
print(MoviesToConvert)
print(f"There's all the files to reencode")

for j in MoviesToConvert:
    print(f"Reencoding {start_dir}\\{j} vers {start_dir}\\{j}")
    original_file_title = j.split('.')[0]
    command = f'{start_dir}\\ffmpeg -i "{start_dir}\\{j}" -c:v libx264 -c:a aac -crf 22 "{start_dir}\\Web_{original_file_title}.mkv"'
    os.system(command)
    os.remove(f"{start_dir}\\{j}")
    os.rename(f"{start_dir}\\Web_{original_file_title}.mkv", f"{start_dir}\\{original_file_title}.mkv")
