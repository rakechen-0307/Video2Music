import os
from video2music import Video2music

input_primer = "C Am F G"
input_key = "C major"
video2music = Video2music(device='cpu')

video_dir = "../samples/videos"
output_dir = "./v2m"
files = sorted(os.listdir(video_dir))
for i in range(len(files)):
    file_id = files[i].split('.')[0]
    input_video = os.path.join(video_dir, files[i])
    output_filename = video2music.generate(input_video, input_primer, input_key)
    os.system("mv {source} {output}".format(
        source="./output/output.mp4",
        output=os.path.join(output_dir, f"{file_id}.mp4")
    ))