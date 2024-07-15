import os
import shutil
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Function to recognize Spanish words from audio file
def recognize_spanish_word(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            recognized_text = recognizer.recognize_google(audio_data, language='es-ES')
            return recognized_text
        except sr.UnknownValueError:
            print("Unable to recognize speech")
            return None

# Function to convert filename to Spanish word and save as mp3
def convert_filename_to_spanish(input_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    unrecognized_dir = os.path.join(output_dir, "unrecognized")
    os.makedirs(unrecognized_dir, exist_ok=True)
    
    # List all files in input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".wav"):
            input_path = os.path.join(input_dir, filename)
            # Load audio file
            audio = AudioSegment.from_wav(input_path)
            # Split audio on silence
            chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)
            # Extract audio chunks and recognize Spanish words
            for i, chunk in enumerate(chunks):
                # Export chunk as WAV
                chunk.export("temp.wav", format="wav")
                # Recognize Spanish word from chunk
                spanish_word = recognize_spanish_word("temp.wav")
                if spanish_word:
                    # Check if the file already exists
                    output_file = os.path.join(output_dir, f"{spanish_word}_{i}.mp3")
                    count = 1
                    while os.path.exists(output_file):
                        output_file = os.path.join(output_dir, f"{spanish_word}_{i}_{count}.mp3")
                        count += 1
                    chunk.export(output_file, format="mp3")
                    print(f"Copied and renamed '{filename}' to '{os.path.basename(output_file)}'")
                else:
                    # Unrecognized file
                    unrecognized_output_path = os.path.join(unrecognized_dir, filename)
                    shutil.copy(input_path, unrecognized_output_path)
                    print(f"Unrecognized: '{filename}'")
            # Remove temporary WAV file
            os.remove("temp.wav")

# Paths
input_directory = r"D:\Yash\Major Project Docs\Spanish\wavs"
output_directory = r"D:\Yash\Major Project Docs\Spanish\wavs\new"

# Convert filenames to Spanish words and save as mp3
convert_filename_to_spanish(input_directory, output_directory)
