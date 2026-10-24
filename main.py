import asyncio
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
from deep_translator import GoogleTranslator

def speak(text, language = "en"):
    engine=pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty('voices')

    if language=="en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Please speak now in English.... ")
        audio=recognizer.listen(source)

    try:
        print("???? Recognizing speech.... ")
        text=recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""

def translate_text(text, target_language="hi"):

    try:

        print("Translating English to", target_language, "...")

        translator = GoogleTranslator(source="en",target=target_language)

        translated_text = translator.translate(text)

        print("English:", text)

        print("Translated text:", translated_text)

        return translated_text

    except Exception as error:

        print("Translation failed:", error)

    return ""

def display_language_options():
    print("🌍 Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")

    choice = input("Please select the target language number (1-8): ")
    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }
    
    return language_dict.get(choice)

def main():
    target_language = display_language_options()
    
    original_text = speech_to_text()
    
    if original_text:
        translated_text =translate_text(original_text, target_language=target_language)
        
        speak(translated_text, language=target_language) 
        print("✅ Translation spoken out!")

if __name__ == "__main__":
    main()