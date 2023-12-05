import datetime

def greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning" if language == "English" else "Bonjour"
    elif 12 <= current_hour < 18:
        return "Good afternoon" if language == "English" else "Bon après-midi"
    else:
        return "Good evening" if language == "English" else "Bonsoir"

def farewell():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Goodbye" if language == "English" else "Au revoir"
    elif 12 <= current_hour < 18:
        return "Have a good day" if language == "English" else "Bonne journée"
    else:
        return "Good night" if language == "English" else "Bonne nuit"

def is_palindrome(text):
    return text == text[::-1]



language = input("Choix du langage / Choose your language (English/Français): ").capitalize()

print(greeting())

while True:
    user_input = input("Enter text (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print(farewell())
        break
    elif is_palindrome(user_input.replace(" ", "").lower()):
        print("Bien dit!" if language == "Français" else "Well said!")
    else:
        print(user_input)  # Mirror response
