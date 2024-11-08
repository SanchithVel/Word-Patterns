# ANSI escape code constant defintions to add color to console output
RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"
def reverseText(text):
    """
    Reverses the given text by slicing it from the end to the start.
    
    Parameters:
        text (str): The string to be reversed.
    
    Returns:
        str: The reversed string -> reversedText.
    """
    #text[::-1] starts at the end of the string and ends at position 0, moving with a step of -1, which returns the in reverse
    reversedText = text[::-1] 
    return reversedText

def isPalindrome(text):
    """
    Checks if the given text is a palindrome (ignoring case and spaces).

    A palindrome is a word or phrase that reads the same forward and backward, ignoring spaces.

    Parameters:
        text (str): The string to be checked for palindrome status -> text.

    Returns:
        None
    """

    # Convert the text to uppercase and strip any extra spaces
    textInReverse = (reverseText(text).upper()).strip()
    inputText = (text.upper()).strip()

    if " " in text.strip():
        if textInReverse.replace(" ", "") == inputText.replace(" ", ""):
            print(GREEN + "\nPhrase IS a palindrome" + RESET)
        else:
            print(RED + "\nPhrase is NOT a palindrome" + RESET)
    else:    
        if textInReverse == inputText:
            print(GREEN + "\nWord IS a palindrome" + RESET)
        else:
            print(RED + "\nWord is NOT a palindrome" + RESET)

def alternatingCapitalization(text):
    """
    Alternates the capitalization of characters in the given text, ignoring spaces.

    Parameters:
        text (str): The string to be modified with alternating capitalization -> text.

    Returns:
        str: The string with alternating capitalization -> newAlternatingWord.
    """
    newAlternatingWord = ""
    count = 0  # Counter to track the position for alternating case, ignoring spaces
    for x in range(len(text)):
        if text[x] == " ":  # If it's a space, add it unchanged
            newAlternatingWord += " "
        else:
            if count % 2 == 0:
                newAlternatingWord += text[x].upper()
            else:
                newAlternatingWord += text[x].lower()
            count += 1  # Only increment count for non-space characters

    return newAlternatingWord

def areAnagrams(text):
    """
    Checks if two words or phrases are anagrams of each other.

    Anagrams are words or phrases that have the same letters in a different arrangement.

    Parameters:
        text (str): Input string containing two comma-separated words.

    Returns:
        None
    """
    # Split the input by comma and strip any extra spaces
    text1, text2 = [word.strip() for word in text.split(",")]
    
    # If both text have their characters sorted alphabetically, are they equal ignoring spaces
    if sorted(text1.replace(" ", "").lower()) == sorted(text2.replace(" ", "").lower()):
        print("\n" + GREEN + f"'{text1}' and '{text2}' ARE anagrams" + RESET)
    else:
        print("\n" + GREEN + f"'{text1}' and '{text2}' are NOT anagrams" + RESET)
def displayMenu():
    """
    Prints the menu options for the user to select from.

    Prints the numbered menu options in blue and the exit option in orange.
    """
    print("\nWhat operation would you like to perform on the text?")
    print(BLUE + "1. Reverse word/phrase")
    print("2. Check for word palindrome or phrase palindrome")
    print("3. Alternating capitalization on word/sentence")
    print("4. Check if two words/phrases are anagrams" + RESET)
    print(ORANGE + "5. Exit program" + RESET)

# Main program
while True:
    # Display the menu options first
    displayMenu()

    # Get the user's choice
    choice = input("Enter the number of the operation (1-5): ")

    # Input validation: input must be digit from 1-5
    if not choice.isdigit() or not (1 <= int(choice) <= 5):
        print(RED + "\nInvalid choice. Please enter an integer between 1 and 5." + RESET)
        continue

    # Exit if the user selects option 5
    if choice == '5':
        print("Exiting program.")
        break # Exits the loop/program

    if choice == '4': 
            # Seperate input system for areAnagrams function as it can include comma characters
            wordsForAnagram = input("Enter two words or phrases separated by a comma (e.g., word1, word2): ") 

            # Checking if input is valid (space, alphabet, or comma)
            if not all(char.isalpha() or char.isspace() or char == ',' for char in wordsForAnagram):
                print(RED + "\nInput word should only contain alphabetic characters, spaces, and commas. Please try again." + RESET)
                continue
            else:
                areAnagrams(wordsForAnagram) # Function already prints the result
                continue

    # Ask for input for the operations reverse text, palindrome, or alternating capitalization
    textForOperation = input("Enter a word or phrase to be operated on (only alphabetic characters and spaces allowed): ")

    # Input validation: Ensure the input is a valid string of alphabetic characters
    if not all(char.isalpha() or char.isspace() for char in textForOperation):
        print(RED + "\nInput word should only contain alphabetic characters and spaces. Please try again." + RESET)
        continue

    # Perform the corresponding operation based on user input
    if choice == '1':
        print(GREEN + "\nReversed text:", reverseText(textForOperation) + RESET)
    elif choice == '2':
        isPalindrome(textForOperation) # Function already prints the result
    elif choice == '3':
        print(GREEN + "\nText with alternating capitalization: ", alternatingCapitalization(textForOperation) + RESET)
