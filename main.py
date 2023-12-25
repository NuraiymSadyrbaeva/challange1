import random

# Funktion, um eine passende Antwort zu generieren
def get_response(user_input):
    responses = [
        "Hallo! Wie kann ich dir helfen?",
        "Schön, dass du da bist!",
        "Ich bin ein einfacher Chatbot. Frag mich etwas!",
        "Wie geht es dir heute?"
    ]
    return random.choice(responses)

# Hauptschleife des Chatbots
print("Willkommen! Schreibe 'bye', um den Chat zu beenden.")
while True:
    user_input = input("Du: ")
    user_input = user_input.lower()

    if user_input == 'bye':
        print("Chatbot: Tschüss! Bis zum nächsten Mal.")
        break
    else:
        response = get_response(user_input)
        print("Chatbot:", response)
        #i will try edit with my phone 
#I have to look the code again


