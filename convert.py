import os
from videoprops import get_video_properties

start_dir = "Your path to movies and ffmpeg"
movies = os.listdir(start_dir)
MoviesToConvert = []
for movie in movies:
    try:
        movieStats = get_video_properties(f"{start_dir}\\{movie}")
        print(movieStats['codec_name'], movie)
        if movieStats['codec_name'] != "h264" and movie.endswith(".mkv"):
            MoviesToConvert.append(movie)
    except:
        print(f"Problems with {movie}")
print(f"There's all the files to reencode")
for j in MoviesToConvert:
    print(f"Reencoding {start_dir}\\{j} vers {start_dir}\\Web_{j}")
    command = f'{start_dir}\\ffmpeg -i "{start_dir}\\{j}" -c:v libx264 -c:a copy -crf 22 "{start_dir}\\Web_{j}"'
    os.system(command)
    os.remove(f"{start_dir}\\{j}")
    os.rename(f"{start_dir}\\Web_{j}", f"{start_dir}\\{j}")
