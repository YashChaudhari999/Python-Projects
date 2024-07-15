import os
from pydub import AudioSegment

def mp3_to_wav(mp3_file, wav_file):
    # Load MP3 file
    audio = AudioSegment.from_mp3(mp3_file)
    
    # Export as WAV
    audio.export(wav_file, format="wav")

def convert_all_files_to_wav(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # List all files in the input folder
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        # Check if it's a file
        if os.path.isfile(input_file):
            # Construct paths for input and output files
            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.wav")
            
            # Convert MP3 to WAV
            mp3_to_wav(input_file, output_file)
            print(f"Conversion completed: {input_file} -> {output_file}")

# Example usage
input_folder = r"D:\Yash\Major Project Docs\Spanish"
output_folder = r"D:\Yash\Major Project Docs\Spanish\wavs"

convert_all_files_to_wav(input_folder, output_folder)
