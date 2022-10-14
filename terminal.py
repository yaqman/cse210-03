class TerminalService:
    
    def read_text(self, prompt):
        """
        Args:
         self (TerminalService): An instance of TerminalService.
         prompt (string): The prompt to display on the terminal.

             Returns:
             string: The user's input as text.
        """  
        return input(prompt)
        
    def read_number(self, prompt):
        """
        Args: 
         self (TerminalService): An instance of TerminalService.
         prompt (string): The prompt to display on the terminal.
         
             Returns:
             float: The user's input as a number.
        """
        return float(input(prompt))
           
    def write_text(self, text):
        """
        Args: 
        self (TerminalService): An instance of TerminalService.
        text (string): The text to display.
        """
        print(text)
        
    def write_text_no_new_line(self, text):
        """
        Args: 
        self (Screen): An instance of Screen.
        text (string): The text to display.
        """  
        print (text, end="")
