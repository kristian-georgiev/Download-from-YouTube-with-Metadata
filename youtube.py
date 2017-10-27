#! python2
import youtube_dl
import eyeD3
import pyperclip
options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl': u'%(title)s.%(ext)s',     #name the file the title of the video
    'noplaylist':True,
    'nocheckcertificate':True,
    'addmetadata':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
audio_file=raw_input() #you can paste the link in the terminal
if len(audio_file)<1:
    audio_file=pyperclip.paste() #or press Enter and let the script use your clipboard as input
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([audio_file])
    info_dict = ydl.extract_info(audio_file, download=False)
    video_title = info_dict.get('title', None)
file_input=video_title+'.mp3'
try:
    artist=(video_title.split(' - ')[0]).decode("utf-8") #Since a lot of the titles of the songs I download are in Cyrillic
    title=(''.join(video_title.split(' - ')[1:])).decode("utf-8") #I use this as a workaround
except UnicodeEncodeError:
    artist=raw_input("Artist:") #TODO: implement a (not completely accurate) conversion from Cyrillic to Latin characters.
    title=raw_input("Title:")

tag = eyeD3.Tag()
tag.link(file_input) 
tag.setArtist(artist)
tag.setTitle(title)
tag.update()
print tag.getArtist() #prints the metadata (just for double-checking)
print tag.getTitle()
