import speech_recognition as sr 
import moviepy.editor as mp

#Videonun uzantisina dikkat et!
clip = mp.VideoFileClip('video_recording.mov')
 
clip.audio.write_audiofile('converted.wav')

# Wav dosyası google api kullanılarak okunuyor ve kaydediliyor.. 
r = sr.Recognizer()
audio = sr.AudioFile('converted.wav')
with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)

