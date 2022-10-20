from terminal import TerminalService
from word import Word
from jumper import Jumper

class Director:
    
    def __init__(self):
        self._is_playing = True
        self._jumper = Jumper()
        self._word = Word()
        
    def start_game(self):
        """
        Start the game by running the game main loop
        """
        """
         Args:
         self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()
            self._is_playing = False
 
    def _get_inputs(self):
        self._word.select_word();

    def _do_updates(self):
        pass
    
    def _do_outputs(self):
         self._jumper.draw_jumper()
         self._word.draw_word_guess()