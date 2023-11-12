from random import randint

def choose_category():
    """Allow the user to choose a category from which the word should be picked"""
    print("Welcome to Hangman!")
    print("Choose a category from which the word should be picked:")
    print("1. Birds and animals")
    print("2. Colors")
    print("3. Fruits and vegetables")
    print("4. Car brands")
    category = int(input("Enter your choice (1/2/3/4): ").strip())
    while category < 1 or category > 4:
        print("Please enter an integer from 1 to 4.")
        category = int(input("Enter your choice (1/2/3/4): ").strip())   
    
    if category == 1:
        choice_list = ["Cat", "Dog", "Horse", "Lion", "Elephant", "Giraffe", "Eagle", "Peacock", "Dolphin", "Kangaroo"]
    elif category == 2:
        choice_list = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black", "White"]
    elif category == 3:
        choice_list = ["Apple", "Banana", "Orange", "Grapes", "Strawberry", "Carrot", "Broccoli", "Tomato", "Spinach", "Cucumber"]
    elif category == 4:
        choice_list = ["Toyota", "Honda", "Lamborghini", "Chevrolet", "Jaguar", "Porsche", "Audi", "Volkswagen", "Tesla", "Nissan"]
    
    return choice_list

def pick_word(choice_list):
    """Pick a random word"""
    word = choice_list[randint(0, len(choice_list) - 1)]
    return word

def reveal_chars(word):
    """Randomly reveal some characters of the word"""
    l = len(word)
    revealed = int(l / 2) if l % 2 == 0 else int((l // 2) + 1)  # Number of characters of the word to be revealed
    indexes = []    # Indexes of the characters to be revealed
    for _ in range(revealed):
        rand_i = randint(0, l - 1)
        while rand_i in indexes:
            rand_i = randint(0, l - 1)
        indexes.append(rand_i)
    
    indexes.sort()
    partial_word = []
    for i in range(l):
        if i in indexes:
            partial_word.append(word[i])
        else:
            partial_word.append('_')
    
    print(f"Your word is {partial_word}")

    hidden_chars_indexes = [i for i in range(len(partial_word)) if partial_word[i] == '_']
    hidden_chars = [word[i] for i in hidden_chars_indexes]
    
    return ''.join(partial_word), hidden_chars_indexes, hidden_chars

def guess_word(word, partial_word, hidden_chars_indexes, hidden_chars):
    """Ask the user to guess the word"""
    missing = partial_word.count('_')
    if missing == 1:
        attempts = 2
    else:
        attempts = missing + 2

    print(f"Guess the word now! You have {attempts} attempts.")
    while attempts > 0:
        guess = input("Guess a character: ").strip().lower()
        while len(guess) != 1:
            print("Please enter a single character.")
            guess = input("Guess a character: ").strip()
        
        for i in range(len(word)):
            if word[i].lower() == guess and i in hidden_chars_indexes:
                correct = True
                chars = list(partial_word)
                chars[i] = guess
                partial_word = ''.join(chars)
                char_index = hidden_chars_indexes.index(i)
                hidden_chars_indexes.pop(char_index)
                hidden_chars.pop(char_index)
                break
        else:
            correct = False
            attempts -= 1

        if correct:
            if partial_word.count('_') > 0:
                print(f"Correct! Word is now {partial_word}")
            if partial_word == word:
                print(f"You guessed the word correctly with {attempts} attempt(s) remaining. The word was \"{word}\".")
                break
        else:
            print("Incorrect!")
        
        print(f"{attempts} attempts remaining.")
    else:
        print(f"Sorry, you are out of attempts. The word was \"{word}\".")

if __name__ == '__main__':
    choice_list = choose_category()
    word = pick_word(choice_list)
    partial_word, hidden_chars_indexes, hidden_chars = reveal_chars(word)
    guess_word(word, partial_word, hidden_chars_indexes, hidden_chars)
