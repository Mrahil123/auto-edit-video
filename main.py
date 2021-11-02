from moviepy.editor import *
import os
from datetime import date

video_of_base = VideoFileClip("video.mp4").afx(afx.volumex, 0)

lenn = video_of_base.duration


bgm = AudioFileClip("./bgm.mp3").subclip(0, lenn)


os.mkdir(f"{date.today()}")

langs = ["EN","ES","HI","MR","TA","TE"]
for lang in langs:
    print(f"./voices/{lang} 2021-11-02.mp3")
    voice_over_list = AudioFileClip(f"./voices/{lang} 2021-11-02.mp3")
    clip_v2 =  CompositeAudioClip([voice_over_list,(bgm).fx(afx.volumex, 0.1)]) 
    
    out = video_of_base.set_audio(clip_v2)

    out.write_videofile(f"{date.today()}/{lang}.mp4")









# final_clip = concatenate_videoclips([clip_v2])