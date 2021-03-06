def draw_hangman(tries):
    stages = [
        """ """,
        """
            ----------
            |        |
            |        o
            |       \\|/
            |        |
            |       / \\
            |
            |
         ------   
        
        """,
        """
            ----------
            |        |
            |        o
            |       \|/
            |        |
            |       / 
            |
            |
         ------   
    
        """,
        """
            ----------
            |        |
            |        o
            |       \|/
            |        |
            |       
            |
            |
         ------   
    
        """,
        """
            ----------
            |        |
            |        o
            |       \|
            |        |
            |       
            |
            |
         ------   

        """,
        """
            ----------
            |        |
            |        o
            |        |
            |        |
            |       
            |
            |
         ------   

        """,
        """
            ----------
            |        |
            |        o
            |       
            |        
            |       
            |
            |
         ------   

        """,
        """
            ----------
            |        |
            |        
            |        
            |        
            |       
            |
            |
         ------   

        """
    ]
    return stages[tries]
