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
    word_dict = {}
    
    # List all files in input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp3"):
            input_path = os.path.join(input_dir, filename)
            # Load audio file
            audio = AudioSegment.from_mp3(input_path)
            # Split audio on silence
            chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)
            # Extract audio chunks and recognize Spanish words
            for i, chunk in enumerate(chunks):
                # Export chunk as WAV
                chunk.export("temp.wav", format="wav")
                # Recognize Spanish word from chunk
                spanish_word = recognize_spanish_word("temp.wav")
                if spanish_word:
                    # Check if the Spanish word already exists in the dictionary
                    if spanish_word in word_dict:
                        # If the word exists, increment the count and add it to the filename
                        word_dict[spanish_word] += 1
                        output_path = os.path.join(output_dir, f"{spanish_word}_{word_dict[spanish_word]}.mp3")
                    else:
                        # If it's a new word, add it to the dictionary
                        word_dict[spanish_word] = 0
                        output_path = os.path.join(output_dir, f"{spanish_word}.mp3")
                    shutil.copy(input_path, output_path)
                    print(f"Copied and renamed '{filename}' to '{os.path.basename(output_path)}'")
                else:
                    # If word not recognized, increment count and store in unrecognized directory
                    unrecognized_file = os.path.join(unrecognized_dir, f"unrecognized_{len(os.listdir(unrecognized_dir))}.mp3")
                    shutil.copy(input_path, unrecognized_file)
                    print(f"Unable to recognize speech. Stored '{filename}' in 'unrecognized' folder.")
                # Remove temporary WAV file
                os.remove("temp.wav")

# Paths
input_directory = r"D:\Yash\Major Project Docs\Spanish"
output_directory = r"D:\Yash\Major Project Docs\Spanish\new"

# Convert filenames to Spanish words and save as mp3
convert_filename_to_spanish(input_directory, output_directory)
