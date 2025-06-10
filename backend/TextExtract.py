import os
import whisper

def extract_text(filepath):
    # ✅ Print to verify correct file path
    print(f"Processing file at: {filepath}")

    # ✅ Check if file exists before Whisper tries to read it
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return "Error: File not found."

    model = whisper.load_model("large")
    result = model.transcribe(filepath)
    return result["text"]
