from terminal import TerminalService

class Jumper:
    
    def __init__(self):
        self.terminalService = TerminalService()
        self._jumper = [
            " ___",
            " /___\\",
            " \\ /",
            " \\ /",
            " O",
            " /|\\",
            " / \\",
            "",
            "^^^^^^^"
             ]
             
    def draw_jumper(self):
        for piece in self._jumper:
             self.terminalService.write_text(piece)
    
    def remove_parachute_piece(self):
        self._jumper.pop(0)
        
    def has_parachute(self):
         return len(self.has_parachute) >= 6
         
    def parachute_gone(self):
        self._jumper[0] = " X"