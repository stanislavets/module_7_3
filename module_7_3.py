import io
import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        #print(self.file_names)


    def get_all_words(self):
        all_words = {}
        line3 = []
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    punctuation = r'[,.!?;:"\(\)\[\]\{\}\<\>\/\ - ]'
                    line = re.sub(punctuation, ' ', line)
                    for line2 in line.lower().split():
                        line3.append(line2)
            all_words.update({i: line3})
            line3 = []
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        for k, find_words in all_words.items():
            for i in range(len(find_words)):
                if find_words[i] == word.lower():
                    return {k: i+1}

    def count(self, word):
        count_word = 0
        all_words = self.get_all_words()
        for k, find_words in all_words.items():
            for i in find_words:
                if i == word.lower():
                    count_word += 1
        return {k: count_word}



finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))