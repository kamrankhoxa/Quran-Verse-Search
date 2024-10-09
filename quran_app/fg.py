import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    try:
        # Use the Google Web Speech API for recognition
        text = recognizer.recognize_google(audio_data, language='ar-SA')
        print("Transcript: {}".format(text))
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

if __name__ == "__main__":
    # Replace 'path/to/your/audio/file.wav' with the path to your audio file
    audio_file_path = 'file.wav'

    transcribe_audio(audio_file_path)
