# TODO: Implement the Seeker class as follows...

# 1) Add the class declaration. Use the following class comment.
class Jumper:

    """The figure like of the jumper. more on parts type for line removal
    """
    def __init__(self):
        self.line1 = ["  ___"]

        self.line2_1 = [" /"]
        self.line2_2 = ["___"]
        self.line2_3 = ["\\"]

        self.line3_1 = [" \   "]
        self.line3_2 = ["/"]

        self.line4_1 = ["  \ "]
        self.line4_2 = ["/"]

        self.line5 = ["   0"]

        self.below_head_drawing = ["  /|\\", "  / \\", "       ", "^^^^^^^"]
        
        self.parachute = [self.line1, self.line2_1, self.line2_2, self.line2_3, self.line3_1, self.line3_2, self.line4_1, self.line4_2, self.line5]
        
        self.guess_from_player_is_right = True

        self.line_number = 0

     
#a function to replace characters within parachute and head. it only runs when a guessed character is not withint the random chosen word
    def replace_char_to_space(self, text):

        if "_" in text:
            text = text.replace("_", " ")
        elif "\\" in text:
            text = text.replace("\\", " ")
        elif "/" in text:
            text = text.replace("/", " ")
        elif "0" in text:
            text = text.replace("0", "x")
        return text

    #the lines are replaced based on the replace_char_to_space method. the line_number variables' purpose is to increment the removed lined up to 8 lines. then the game is over.
    def replace_content_of_parachute_based_on_guess_and_line_number(self, parachute, guess_from_player_is_right, line_number):
        extracted_text = ""
        if guess_from_player_is_right:
            pass
        else:
            for text in parachute[line_number]:
                extracted_text = self.replace_char_to_space(text)
                
        
            del parachute[line_number]
            new_list = [extracted_text]
            parachute.insert(line_number, new_list)
            return parachute
        

    #the following methods are only for displaying the parts and text. it gets the updated list based on the replace_content_of_parachute_based_on_guess_and_line_number method
    def replace_drawing_to_space(self, text):
        text_extracted = ""
        if text == "_":
            text_extracted = text.replace("_"," ")
        elif text == "\\":
            text_extracted = text.replace("\\"," ")
        elif text == "/":
            text_extracted = text.replace("/"," ")
        return text_extracted
        

    def draw_line_1(self, parachute):
        text = ""
        for text_in_list in parachute[0]:
            text = text_in_list
        print(text)

    def draw_line_2(self, parachute):
        text1 = ""
        text2 = ""
        text3 = ""
        text = ""
        for text_in_list in parachute[1]:
            text1 = text_in_list

        for text_in_list in parachute[2]:
            text2 = text_in_list

        for text_in_list in parachute[3]:
            text3 = text_in_list
    
        text = text1 + text2 + text3
        print(text)

    def draw_line_3(self, parachute):
        text1 = ""
        text2 = ""
        text = ""
        for text_in_list in parachute[4]:
            text1 = text_in_list

        for text_in_list in parachute[5]:
            text2 = text_in_list


        text = text1 + text2
        print(text)

    def draw_line_4(self, parachute):
        text1 = ""
        text2 = ""
        text = ""
        for text_in_list in parachute[6]:
            text1 = text_in_list

        for text_in_list in parachute[7]:
            text2 = text_in_list


        text = text1 + text2
        print(text)

    def draw_line_5(self, parachute):
        text1 = ""
        for text_in_list in parachute[8]:
            text1 = text_in_list
        text = text1
        print(text)

    def draw_below_head_drawing(self, list):
        for text in list:
            print(text)