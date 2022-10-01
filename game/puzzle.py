from random import randint

class Puzzle:

    def __init__(self):
        #here are the attributes of this class
        self._words = ["responsibility", "books", "common", "travel", "light", "movies", "scorpion", "bleach", "theocracy"]
        self._size_of_words_container = len(self._words)
        self._random_chosen_word_index = randint(0,self._size_of_words_container-1)
        self._random_chosen_word = self._words[self._random_chosen_word_index]
        self._checked_characters_already_entered = []
        self._random_chosen_word_list_container = []
        self._partial_or_complete_guess_word_container = []
        self._guessed_character = ""
        self._checked_characters_already_entered_no_duplicates = []

    #this is for initial game prompt
    def _initial_printing_of_blanks_for_guessing_on_chosen_word(self, text):
        blank_text = ""
        for extracted_character in text:
            if extracted_character == " ":
                blank_text = blank_text + " "
            else:
                blank_text = blank_text + "_" + " "
        return blank_text
    
    #if returned 1, means the value will be equal or greater to one. this is for program to determine if character can be used or not
    def _check_if_character_is_already_entered(self, checked_characters_already_entered, guessed_character):
        zero_or_one = 0
        for extracted_character in checked_characters_already_entered:
            if extracted_character == guessed_character:
                zero_or_one += 1
            else:
                zero_or_one += 0
        return zero_or_one

    
    #returns 0 if the character entered is not found in the text
    def _check_if_guessed_character_is_within_the_random_chosen_word(self, guessed_character, random_chosen_word):
        zero_or_one = 0
        for extracted_character in random_chosen_word:
            
            if extracted_character == guessed_character:
                zero_or_one += 1
            else: 
                zero_or_one += 0
        return zero_or_one
            
        print(text)
                        
    #to append characters entered into array. that array will hold these values to be compare with the length of the word
    def _append_correct_letters_to_checked_characters_already_entered(self, text, character, checked_characters_already_entered):
        for extracted_character in text:
            if extracted_character == character:
                checked_characters_already_entered.append(extracted_character)
            else:
                pass
        return checked_characters_already_entered

    #this is append the characters to a list for comparison and printing it with blankcs.
    def _append_to_random_chosen_word_list_container(self, random_chosen_word, random_chosen_word_list_container):
        for character in random_chosen_word:
            random_chosen_word_list_container.append(character)
        return random_chosen_word_list_container
    
    #this functions was created to append blanks on partial_or_complete_guess_word_container list. this is only for initial blanks
    def _append_blanks(self, random_chosen_word, partial_or_complete_guess_word_container):
        for character in random_chosen_word:
            partial_or_complete_guess_word_container.append("_")
        return partial_or_complete_guess_word_container

        
    #this function is to simply replace the "_" by index number which means it will check the random_chosen_word_list_container and partial_or_complete_guess_word_container back forth
    def _append_correct_letters(self, random_chosen_word_list_container, partial_or_complete_guess_word_container, guessed_character):
        n = 0
        for character in random_chosen_word_list_container:
            if character == guessed_character:
                partial_or_complete_guess_word_container[n] = character
            elif character != "_":
                pass

            n += 1
        return partial_or_complete_guess_word_container


    #this is to print the text in a blank form with spaces for aesthetic purpose only
    def _print_with_blank_form(self, partial_or_complete_guess_word_container):
        text = ""
        for character in partial_or_complete_guess_word_container:
            text = text + character + " "
        print(text)



