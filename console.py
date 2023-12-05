from function import greeting, farewell, is_palindrome
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
