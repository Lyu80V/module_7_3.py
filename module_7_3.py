info = "'file1.txt'"

info_2 = "'file2.txt'"


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self, ):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                line = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(i, '')
                a = line.split()
                all_words[name] = a
        return all_words

    def find(self, word):
        position = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                position[name] = words.index(word.lower()) + 1
            return position

    def count(self, word):
        quantity = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                quantity[name] = words.count(word.lower())
            return quantity


finder2 = WordsFinder(info)
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder2 = WordsFinder(info_2)
print(finder2.get_all_words())  # Все слова
print(finder2.find('CHILD'))  # 3 слово по счёту
print(finder2.count('child'))  # 4 слова teXT в тексте всего