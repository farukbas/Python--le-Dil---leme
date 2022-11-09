import speech_recognition as sr 
import moviepy.editor as mp
import nltk

#Video Dosyası Wav formatına dönüştürülüyor .(video yüklerken uzantisina dikkat edin!)
clip = mp.VideoFileClip('video_recording4.mp4')
 
clip.audio.write_audiofile('converted.wav')

# Wav dosyası google api kullanılarak okunuyor ve kaydediliyor.. 
r = sr.Recognizer()
audio = sr.AudioFile('converted.wav')
with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)


nltk_tokens = nltk.word_tokenize(result)

ordered_tokens = set()
result1 = []
for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result1.append(word)
     

with open('kelimeler.txt', 'w') as file:
    for item in result1:
        file.write("%s\n" % item)     