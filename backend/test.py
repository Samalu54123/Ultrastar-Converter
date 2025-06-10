import whisper
model = whisper.load_model("base")
model.transcribe("path_to_audio_file.mp3")
