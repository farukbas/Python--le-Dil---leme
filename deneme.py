import speech_recognition as sr 
import moviepy.editor as mp

#Video Dosyası Wav formatına dönüştürülüyor .(video yüklerken uzantisina dikkat edin!)
clip = mp.VideoFileClip('video_recording4.mp4')
 
clip.audio.write_audiofile('converted.wav')

# Wav dosyası google api kullanılarak okunuyor ve kaydediliyor.. 
r = sr.Recognizer()
audio = sr.AudioFile('converted.wav')
with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)


sayac=0
for sayac in range(sayac,len(result)):
  print(result[sayac],end="")
  if result[sayac] == " " :
    print("\n")
  sayac += 1