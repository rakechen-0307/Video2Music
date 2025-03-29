from video2music import Video2music

input_video = "../samples/videos/ysSxxIqKNN0.mp4"

input_primer = "C Am F G"
input_key = "C major"

video2music = Video2music(device='cpu')
output_filename = video2music.generate(input_video, input_primer, input_key)