from gtts import gTTS
import os
import requests
from bs4 import BeautifulSoup
import re

# Function to generate audio file for a given Spanish word
def generate_audio(word, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    # Generate audio file path
    audio_file_path = os.path.join(output_dir, f"{word}.mp3")
    # Check if audio file already exists
    if os.path.exists(audio_file_path):
        # Add incremental value until a unique filename is found
        i = 1
        while True:
            new_audio_file_path = os.path.join(output_dir, f"{word}_{i}.mp3")
            if not os.path.exists(new_audio_file_path):
                audio_file_path = new_audio_file_path
                break
            i += 1
    # Create gTTS object with Spanish language
    tts = gTTS(text=word, lang='es-ES')
    # Save audio file
    tts.save(audio_file_path)
    print(f"Audio file generated for '{word}' at '{audio_file_path}'")

# Function to extract Spanish words from a webpage
def extract_spanish_words_from_url(url):
    try:
        # Send GET request to the URL
        response = requests.get(url)
        # Check if request was successful
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract text content from HTML
            text_content = soup.get_text()
            # Find all Spanish words using regex
            spanish_words = re.findall(r'\b[A-ZáéíóúüñÁÉÍÓÚÜÑ]+\b', text_content)
            return spanish_words
        else:
            print("Failed to fetch webpage:", response.status_code)
            return []
    except Exception as e:
        print("Error fetching webpage:", e)
        return []

# URL to fetch the webpage content
url = "https://lingvist.com/course/learn-spanish-online/resources/spanish-preterite/"

# Extract Spanish words from the webpage
spanish_words = extract_spanish_words_from_url(url)

# Generate audio files for each Spanish word
for word in spanish_words:
    generate_audio(word, output_dir=word)  # Save audio files using the same path as the Spanish words
