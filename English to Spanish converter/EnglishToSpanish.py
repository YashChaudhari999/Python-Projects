from gtts import gTTS
import os

# Dictionary mapping English phrases to Spanish phrases
word_dict ={
    "you all will be": "Uds serán"
}



def text_to_audio(text, output_path):
    """
    Converts text to audio and saves it as an mp3 file.
    
    :param text: Text to be converted to audio
    :param output_path: Path where the audio file will be saved
    """
    tts = gTTS(text=text, lang='es-es')  # Specify language as Spanish
    tts.save(output_path)

def convert_text_to_audio_with_translation(text, word_dict, output_directory):
    """
    Converts text to audio using translation dictionary.
    
    :param text: Text to be converted to audio
    :param word_dict: Dictionary containing English to Spanish phrase mappings
    :param output_directory: Directory where audio files will be saved
    """
    for phrase in word_dict:
        if phrase in text:
            translated_text = word_dict[phrase]
            output_filename = f"{phrase}.mp3"
            output_path = os.path.join(output_directory, output_filename) 
            
            # Check if the file already exists
            if os.path.exists(output_path):
                # If file exists, append a number to the filename
                count = 1
                while os.path.exists(os.path.join(output_directory, f"{phrase}_{count}.mp3")):
                    count += 1
                output_filename = f"{phrase}_{count}.mp3"
                output_path = os.path.join(output_directory, output_filename)
                
            text_to_audio(translated_text, output_path)
            print(f"Audio file saved for '{phrase}' at: {output_path}")

# Example usage
text = "you all will be"
output_directory = r"D:\Yash\Major Project Docs\Spanish"

convert_text_to_audio_with_translation(text, word_dict, output_directory)