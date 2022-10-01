from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:


    def __init__(self):
        # to declare the director class
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
    #most of the scripts below are from puzzle and jumper
        
    def start_game(self):

        self._terminal_service.write_text(self._puzzle._initial_printing_of_blanks_for_guessing_on_chosen_word(self._puzzle._random_chosen_word))
        self._terminal_service.write_text("")
        self._draw_parachute_and_body()
        self._puzzle._guessed_character = self._terminal_service.read_text("Please choose from letter A to Z: ")
        self._puzzle._random_chosen_word_list_container = self._puzzle._append_to_random_chosen_word_list_container(self._puzzle._random_chosen_word, self._puzzle._random_chosen_word_list_container)
        self._puzzle._partial_or_complete_guess_word_container = self._puzzle._append_blanks(self._puzzle._random_chosen_word, self._puzzle._partial_or_complete_guess_word_container)
        character_is_in_random_word = self._puzzle._check_if_guessed_character_is_within_the_random_chosen_word(self._puzzle._guessed_character, self._puzzle._random_chosen_word)
        
        
        check_one_or_zero = self._puzzle._check_if_character_is_already_entered(self._puzzle._checked_characters_already_entered, self._puzzle._guessed_character)
        #check zero or one means if the character is already entered. if yes. the program will not accept and allows you to enter a character again.
        if check_one_or_zero > 0:
            self._terminal_service.write_text("This character was already entered")
        else:
            self._puzzle._checked_characters_already_entered = self._puzzle._append_correct_letters_to_checked_characters_already_entered(self._puzzle._random_chosen_word, self._puzzle._guessed_character, self._puzzle._checked_characters_already_entered)

        if character_is_in_random_word == 1:
            pass
        else:
            self._jumper.guess_from_player_is_right = False
            self._jumper.replace_content_of_parachute_based_on_guess_and_line_number(self._jumper.parachute, self._jumper.guess_from_player_is_right, self._jumper.line_number)
            self._jumper.line_number = self._jumper.line_number + 1
            
        self._do_updates()
        self._draw_parachute_and_body()
        self._do_outputs()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._draw_parachute_and_body()
            self._do_outputs()



    def _get_inputs(self):
        self._puzzle._guessed_character = self._terminal_service.read_text("Please choose from letter A to Z: ")
        check_one_or_zero = self._puzzle._check_if_character_is_already_entered(self._puzzle._checked_characters_already_entered, self._puzzle._guessed_character)
        
        if check_one_or_zero > 0:
            self._terminal_service.write_text("This character was already entered")
        else:
            self._puzzle._checked_characters_already_entered = self._puzzle._append_correct_letters_to_checked_characters_already_entered(self._puzzle._random_chosen_word, self._puzzle._guessed_character, self._puzzle._checked_characters_already_entered)

        character_is_in_random_word = self._puzzle._check_if_guessed_character_is_within_the_random_chosen_word(self._puzzle._guessed_character, self._puzzle._random_chosen_word)
        if character_is_in_random_word >= 1:
            pass
        else:
            self._jumper.guess_from_player_is_right = False
            self._jumper.replace_content_of_parachute_based_on_guess_and_line_number(self._jumper.parachute, self._jumper.guess_from_player_is_right, self._jumper.line_number)
            self._jumper.line_number = self._jumper.line_number + 1
        
    def _do_updates(self):
        self._puzzle._partial_or_complete_guess_word_container = self._puzzle._append_correct_letters(self._puzzle._random_chosen_word_list_container, self._puzzle._partial_or_complete_guess_word_container, self._puzzle._guessed_character)
        
                
    def _do_outputs(self):
        
        self._puzzle._print_with_blank_form(self._puzzle._partial_or_complete_guess_word_container)
        
        if len(self._puzzle._checked_characters_already_entered) == len(self._puzzle._random_chosen_word):
            self._terminal_service.write_text("Congratulations! You successfully guessed the right word!")
            self._is_playing = False
        elif self._jumper.line_number == 8:
            self._jumper.guess_from_player_is_right = False
            self._jumper.replace_content_of_parachute_based_on_guess_and_line_number(self._jumper.parachute, self._jumper.guess_from_player_is_right, self._jumper.line_number)
            self._draw_parachute_and_body()
            self._terminal_service.write_text("Game over! You failed to guess the right word.")
            self._is_playing = False
        

    def _draw_parachute_and_body(self):
        self._jumper.draw_line_1(self._jumper.parachute)
        self._jumper.draw_line_2(self._jumper.parachute)
        self._jumper.draw_line_3(self._jumper.parachute)
        self._jumper.draw_line_4(self._jumper.parachute)
        self._jumper.draw_line_5(self._jumper.parachute)
        self._jumper.draw_below_head_drawing(self._jumper.below_head_drawing)