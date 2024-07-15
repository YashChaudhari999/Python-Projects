from gtts import gTTS
import os

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

# Directory to save audio files
output_directory = r"D:\Yash\Major Project Docs\Spanish\wavs\new"

# Input Spanish words (you can replace this list with your own words)
spanish_words = spanish_words =  [
    "Hijo de puta ",
    " Hijo de perra",
    " Qué estás haciendo, güey  ",
    "Pomo",
    "Culo",
    "Culero",
    "Pendejo",
    "Chingar",
    "Cabrón",
    "Huevo",
    "Verga",
    " A la verga!",
    "Panocha",
    "Cochino",
    "Chaqueta",
    "Gandalla"

    
    " Bueno!  Con quién tengo el gusto de hablar  ",
    " Oye wey, vamos a comer cochinita pibil!",
    " Qué onda, ese    Cómo estás  ",
    "Ese chavo es muy amable.",
    " Hola, amigo!  Qué pasó contigo hoy  ",
    " Qué onda, compa    Vamos al partido  ",
    " No manches, ganamos el partido!",
    " Órale, vamos a la playa!",
    "Me dijo que vienen a visitarnos.",
    "  Mande  ",
    "Gané la lotería! ",
    "  Neta  ",
    " Órale, nos vemos allí a las siete.",
    "Ya estás, no me hables así.",
    "Esa camiseta que compraste es bien chanclas.",
    "No puedo ir al trabajo hoy, estoy crudo.",
    "Debes vigilar a tu amigo, se pone malacopa después de unas cervezas.",
    "Suave, no te preocupes tanto.",
    " Pinche tráfico, siempre tan pesado!",
    "No compres esa computadora, es bien chafa.",
    "Lo siento, caguéla con el informe de ayer.",
    "La cagó en el examen de matemáticas.",
    " Quién la cagó con la preparación del proyecto  ",
    "El vendedor me cagó con la calidad de este producto.",
    " Qué pedo, cómo has estado  ",
    "Le presté mi auto y me lo regresó con un rayón, pero le dije que no hay pedo.",
    "No recuerdo nada de lo que pasó anoche, andaba bien pedo.",
    " No mames, ganamos el premio mayor!",
    "Madres, olvidé mi billetera en casa.",
    "Me vale madres lo que piensen los demás de mí.",
    " Puta madre, se me olvidaron las llaves adentro del carro!",
    "Esa banda de rock es poca madre,  tienen un sonido increíble!",
    "Ese tipo es un perro, siempre encuentra la manera de salirse con la suya.",
    "Ese tipo es un verdadero hijo de puta, no se puede confiar en él.",
    " Qué estás haciendo, güey   Vamos a jugar videojuegos.",
    "Vamos al pomo esta noche, va a estar muy divertido.",
    "Me caí y me golpeé el culo.",
    "Ese tipo es muy culero, siempre está buscando problemas.",
    "No seas pendejo, sabes que eso no es verdad.",
    "Estoy cansado de chingar todo el día.",
    "Ese boxeador es bien cabrón, nunca se rinde en el ring.",
    "Me lastimé los huevos jugando fútbol.",
    " Qué verga, olvidé mi cartera en casa!",
    " A la verga con esta situación, no puedo más!",
    "Limpia tu cuarto. Está bien cochino.",
    "Deja de hacer chaqueta y ponte a trabajar en tus tareas.",
    "No seas gandalla, comparte tus juguetes con tu hermano."
]

# Generate audio files for each Spanish word
for word in spanish_words:
    generate_audio(word, output_directory)
