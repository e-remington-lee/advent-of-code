from pathlib import Path



class Solution():
    def __init__(self, input_text_file):
        self.map = self._create_map(input_text_file)
        self.search_word = "XMAS"
        self.matches = 0


    def _create_map(self, input_text_file):
        words = []
        INPUT_PATH = Path(__file__).parent / input_text_file
        with open(INPUT_PATH, "r") as file:
            # can optimize the read portion here
            for line in file:
                words.append(list(line.strip()))
        return words

    def search_map(self):
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] != self.search_word[0]:
                    continue
                self.matches += self._perform_search(row, col, 'right')
                self.matches += self._perform_search(row, col, 'left')
                self.matches += self._perform_search(row, col, 'up')
                self.matches += self._perform_search(row, col, 'down')
                self.matches += self._perform_search(row, col, 'up_right')
                self.matches += self._perform_search(row, col, 'up_left')
                self.matches += self._perform_search(row, col, 'down_right')
                self.matches += self._perform_search(row, col, 'down_left')
        return self.matches

    #part 1
    def _perform_search(self, row, col, direction):
            hi = 0 
            vi = 0
            if direction == 'right':
                hi = 1
                vi = 0
            if direction == 'left':
                hi = -1
                vi = 0
            if direction == 'up':
                hi = 0
                vi = -1
            if direction == 'down':
                hi = 0
                vi = 1
            if direction == 'up_right':
                hi = 1
                vi = -1
            if direction == 'down_right':
                hi = 1
                vi = 1
            if direction == 'up_left':
                hi = -1
                vi = -1
            if direction == 'down_left':
                hi = -1
                vi = 1

            for i in range(1, len(self.search_word)):
                if ((row + i*vi >= len(self.map[col])) or row + i*vi <0) or (col + i*hi >= len(self.map) or col + i*hi < 0):
                    return 0
                if self.map[row + i*vi][col + i*hi] != self.search_word[i]:
                    return 0
            print(f"Found {self.search_word} at {row}, {col} going {direction}")
            return 1
    
    #part2
    def _perform_search2(self, row, col):
            ur = [-1, 1]
            ul = [-1, -1]
            dr = [1, 1]
            dl = [1, -1]

            if ((row + 1 >= len(self.map[col])) or row + 1 < 0) or (col + 1 >= len(self.map) or col + 1 < 0):
                return 0
            if (self.map[row + ur[0]][col + [ur[1]]] == "")
            print(f"Found {self.search_word} at {row}, {col}")
            return 0
                
sol = Solution("day4_input.txt")
print(sol.search_map())