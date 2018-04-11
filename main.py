import os

urls = [

];

for song in urls:
    os.system('youtube-dl --extract-audio --audio-format mp3 %s' % song);
