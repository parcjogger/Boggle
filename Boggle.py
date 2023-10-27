import random
from Paths import Word_Searcher
from scrabble_words import all_words

class Boggle_Game:
    
     dice = ['rifobx', 'ifehey', 'denows', 'utoknd', 'hmsrao', 'lupets', 'acitoa', 'ylgkue', '*bmjoa', 'ehispn',
            'vetign', 'baliyt', 'ezavnd', 'ralesc', 'uwilrg', 'pacemd']

     def __init__(self):
        self.minimum_word_length = 3
        self.initialize_boggle_letters()
        self.print_boggle_board()
       
     def initialize_boggle_letters(self):
        boggle_letters = []
        for i in range(16):
            random_letter = random.sample(self.dice[i],1)
            if random_letter[0] == '*':
                random_letter = ['qu']
            boggle_letters = boggle_letters + random_letter #does boggle_letter need to be defined?
        random.shuffle(boggle_letters)
        self.boggle_letters = boggle_letters

     def print_boggle_board(self):
         boggle_letters = self.boggle_letters.copy()
         for i in range(16):
             boggle_letter = boggle_letters[i]
             boggle_letter = boggle_letter.upper()
             boggle_letters[i] = boggle_letter
         print(boggle_letters[0], boggle_letters[1], boggle_letters[2], boggle_letters[3])
         print(boggle_letters[4], boggle_letters[5], boggle_letters[6], boggle_letters[7])
         print(boggle_letters[8], boggle_letters[9], boggle_letters[10], boggle_letters[11])
         print(boggle_letters[12], boggle_letters[13], boggle_letters[14], boggle_letters[15])
         

bg = Boggle_Game()
ws = Word_Searcher()
ws.update_nodes(bg.boggle_letters)
ws.update_graph()
ws.update_dictionary(bg.boggle_letters)
ws.update_paths()
ws.search_path_for_words()
ws.print_words()

