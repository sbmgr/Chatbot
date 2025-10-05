import speech_recognition as sr
import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

recognizer = sr.Recognizer()

def listen_and_respond():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Chatbot is listening. Say 'bye' to exit.")
        while True:
            try:
                print("\nListening...")
                audio = recognizer.listen(source, phrase_time_limit=5)
                text = recognizer.recognize_google(audio).lower()
                print(f"You said: {text}")

                response = chatbot_response(text)
                print(f"Bot: {response}")
                speak(response)

                if "bye" in text:
                    print("Exiting chatbot...")
                    break

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Could not request results from Google STT service.")

def chatbot_response(user_input):
    if "hello" in user_input:
        return "Hello! How are you today?"
    elif "your name" in user_input:
        return "I am your friendly Python chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

def main():
    listen_and_respond()

if __name__ == "__main__":
    main()