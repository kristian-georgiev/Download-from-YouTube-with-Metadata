import youtube_dl
import eyeD3
options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl': u'%(title)s.%(ext)s',     #name the file the ID of the video
    'noplaylist':True,
    'nocheckcertificate':True,
    'addmetadata':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
audio_file=raw_input()
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([audio_file])
    info_dict = ydl.extract_info(audio_file, download=False)
    video_title = info_dict.get('title', None)
file_input=video_title+'.mp3'
try:
    artist=(video_title.split(' - ')[0]).decode("utf-8")
    title=(''.join(video_title.split(' - ')[1:])).decode("utf-8")
except UnicodeEncodeError:
    artist=raw_input("Artist:")
    title=raw_input("Title:")

tag = eyeD3.Tag()
tag.link(file_input)
tag.setArtist(artist)
tag.setTitle(title)
tag.update()
print tag.getArtist()
print tag.getTitle()
