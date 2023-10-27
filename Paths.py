from scrabble_words import all_words

class Word_Searcher:
    def __init__(self):
        self.initialize_nodes()
        self.initialize_graph()
        self.paths = []
        self.extended_paths = []
        self.dictionary = {}
        self.words = []
        self.word_length = 3
            
    def initialize_nodes(self):
        self.nodes = []
        for i in range(16):
             node = (i, None)
             self.nodes.append(node)
        
    def initialize_graph(self):
       self.graph = {self.nodes[0] : [self.nodes[1], self.nodes[4], self.nodes[5]],
                    self.nodes[1] : [self.nodes[0], self.nodes[2], self.nodes[4], self.nodes[5], self.nodes[6]],
                    self.nodes[2] : [self.nodes[1], self.nodes[3], self.nodes[5], self.nodes[6], self.nodes[7]],
                    self.nodes[3] : [self.nodes[2], self.nodes[6], self.nodes[7]],
                    self.nodes[4] : [self.nodes[0], self.nodes[1], self.nodes[5], self.nodes[8], self.nodes[9]],
                    self.nodes[5] : [self.nodes[0], self.nodes[1], self.nodes[2], self.nodes[4], self.nodes[6], self.nodes[8], self.nodes[9], self.nodes[10]],
                    self.nodes[6] : [self.nodes[1], self.nodes[2], self.nodes[3], self.nodes[5], self.nodes[7], self.nodes[9], self.nodes[10], self.nodes[11]],
                    self.nodes[7] : [self.nodes[2], self.nodes[3], self.nodes[6], self.nodes[10], self.nodes[11]],
                    self.nodes[8] : [self.nodes[4], self.nodes[5], self.nodes[9], self.nodes[12], self.nodes[13]],
                    self.nodes[9] : [self.nodes[4], self.nodes[5], self.nodes[6], self.nodes[8], self.nodes[10], self.nodes[12], self.nodes[13], self.nodes[14]],
                    self.nodes[10] : [self.nodes[5], self.nodes[6], self.nodes[7], self.nodes[9], self.nodes[11], self.nodes[13], self.nodes[14], self.nodes[15]],
                    self.nodes[11] : [self.nodes[6], self.nodes[7], self.nodes[10], self.nodes[14], self.nodes[15]],
                    self.nodes[12] : [self.nodes[8], self.nodes[9], self.nodes[13]],
                    self.nodes[13] : [self.nodes[8], self.nodes[9], self.nodes[10], self.nodes[12], self.nodes[14]],
                    self.nodes[14] : [self.nodes[9], self.nodes[10], self.nodes[11], self.nodes[13], self.nodes[15]],
                    self.nodes[15] : [self.nodes[10],self.nodes[11],self.nodes[14]]
                    }

    def update_nodes(self, boggle_letters):
        for i in range(16):
            self.nodes[i] = (i, boggle_letters[i])
    
    def update_graph(self):
        self.graph = {self.nodes[0] : [self.nodes[1], self.nodes[4], self.nodes[5]],
                    self.nodes[1] : [self.nodes[0], self.nodes[2], self.nodes[4], self.nodes[5], self.nodes[6]],
                    self.nodes[2] : [self.nodes[1], self.nodes[3], self.nodes[5], self.nodes[6], self.nodes[7]],
                    self.nodes[3] : [self.nodes[2], self.nodes[6], self.nodes[7]],
                    self.nodes[4] : [self.nodes[0], self.nodes[1], self.nodes[5], self.nodes[8], self.nodes[9]],
                    self.nodes[5] : [self.nodes[0], self.nodes[1], self.nodes[2], self.nodes[4], self.nodes[6], self.nodes[8], self.nodes[9], self.nodes[10]],
                    self.nodes[6] : [self.nodes[1], self.nodes[2], self.nodes[3], self.nodes[5], self.nodes[7], self.nodes[9], self.nodes[10], self.nodes[11]],
                    self.nodes[7] : [self.nodes[2], self.nodes[3], self.nodes[6], self.nodes[10], self.nodes[11]],
                    self.nodes[8] : [self.nodes[4], self.nodes[5], self.nodes[9], self.nodes[12], self.nodes[13]],
                    self.nodes[9] : [self.nodes[4], self.nodes[5], self.nodes[6], self.nodes[8], self.nodes[10], self.nodes[12], self.nodes[13], self.nodes[14]],
                    self.nodes[10] : [self.nodes[5], self.nodes[6], self.nodes[7], self.nodes[9], self.nodes[11], self.nodes[13], self.nodes[14], self.nodes[15]],
                    self.nodes[11] : [self.nodes[6], self.nodes[7], self.nodes[10], self.nodes[14], self.nodes[15]],
                    self.nodes[12] : [self.nodes[8], self.nodes[9], self.nodes[13]],
                    self.nodes[13] : [self.nodes[8], self.nodes[9], self.nodes[10], self.nodes[12], self.nodes[14]],
                    self.nodes[14] : [self.nodes[9], self.nodes[10], self.nodes[11], self.nodes[13], self.nodes[15]],
                    self.nodes[15] : [self.nodes[10],self.nodes[11],self.nodes[14]]
                    }
    
    def update_paths(self):
        self.paths = [[self.nodes[0]]]
    
    def update_dictionary(self, boggle_letters):
         boggle_letters_set = set(boggle_letters)
         for boggle_letter in boggle_letters_set:
           boggle_letter_word_list = []
           for word in all_words: 
            if word[0] == boggle_letter[0]:
                boggle_letter_word_list.append(word)
           self.dictionary.update({boggle_letter : boggle_letter_word_list}) 

    def search_path_for_words(self):
        while(True):
            for path in self.paths:
                self.create_extended_paths(path, self.get_path_neighbors(path))
                self.check_extended_paths_for_possible_words(self.extended_paths)
                self.check_extended_paths_for_words(self.extended_paths)
                self.reset_paths_and_extended_paths()
                if self.paths == []:
                    return
            
    def get_path_neighbors(self, path):
        path_length = len(path)
        current_path_end = path[path_length - 1]
        path_neighbors = self.graph.get(current_path_end) #neighbors is list of self.nodes
        temp_path_neighbors = []
        for path_neighbor in path_neighbors:
            if path_neighbor not in path:
                temp_path_neighbors.append(path_neighbor)
        path_neighbors = temp_path_neighbors
        return path_neighbors
    
    def create_extended_paths(self, path, path_neighbors):
        if path_neighbors == []:
            return
        for path_neighbor in path_neighbors :
            extended_path = path + [path_neighbor]
            self.extended_paths.append(extended_path)

    def check_extended_paths_for_possible_words(self, extended_paths):
         if(extended_paths == []):
             return
         extended_paths_possible_word = []
         for extended_path in extended_paths:
              possible_word = self.extract_possible_word_from_path(extended_path) #extended path is a list of self.nodes
              if (self.is_possible_word(possible_word)) == True:
                extended_paths_possible_word.append(extended_path)
         self.extended_paths = extended_paths_possible_word 
         
    def check_extended_paths_for_words(self, extended_paths):
         if(extended_paths == []):
             return
         for extended_path in extended_paths:
            if len(extended_path) >= self.word_length:
                possible_word = self.extract_possible_word_from_path(extended_path) #extended path is a list of self.nodes
                if self.is_word(possible_word) == True:
                    self.words.append(possible_word) 
    
    def extract_possible_word_from_path(self, path):    #path is a list of self.nodes
        possible_word = ''
        for node in path:
            possible_word = possible_word + node[1]  
        return possible_word
    
    def is_possible_word(self, possible_word):
        initial_letter_of_possible_word = possible_word[0]
        length_of_possible_word = len(possible_word)
        initial_letter_word_list = self.dictionary[initial_letter_of_possible_word]
        for word in initial_letter_word_list:
            if possible_word == word[0 : length_of_possible_word]:
                return True
        return False
    
    def is_word(self, possible_word):
        initial_letter_of_possible_word = possible_word[0]
        initial_letter_word_list = self.dictionary[initial_letter_of_possible_word] 
        for word in initial_letter_word_list:
            if possible_word == word:
                return True
        return False
    
    def reset_paths_and_extended_paths(self):
        self.paths = []
        self.paths = self.extended_paths
        self.extended_paths = []

    def print_words(self):
        print(self.words)