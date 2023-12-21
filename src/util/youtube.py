from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=kTK-TRNpqTA&ab_channel=AmazonPrimeVideoUK%26IE')

title = yt.title
streams = yt.streams.filter(file_extension='mp4', progressive=True)
stream = yt.streams.get_by_itag(251)
stream.download(output_path="./", filename="video-144p.wav")
print(title)