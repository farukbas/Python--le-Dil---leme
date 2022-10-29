import speech_recognition as sr 
import moviepy.editor as mp


clip = mp.VideoFileClip('video_recording.mov')
 
clip.audio.write_audiofile('converted.wav')


