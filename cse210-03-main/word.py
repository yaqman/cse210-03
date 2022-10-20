from terminal import TerminalService

class Word:
    def __init__(self):
        self.terminalService = TerminalService()
        self._word_list = [""]
        self._word_selected = ""
        self.select_word()
        self._word_guess = ["_"] * len(self._word_selected)
        
    def select_word(self):
        self._word_guess = input("Guess a letter [a-z]: ")

    def draw_word_guess(self):
        for i in self._word_guess:
            self.terminalService.write_text_no_new_line(i + " ")