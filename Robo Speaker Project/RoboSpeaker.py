import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to RoboSpeaker 1.2 Created by Yash")
    
    while True:
        x = input("Enter what you want me to speak: ")
        engine.say(x)
        engine.runAndWait()
        engine.stop()