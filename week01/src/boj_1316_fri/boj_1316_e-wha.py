class group_word:
    def __init__(self, N, words):
        self.N = N
        self.words = words

    def word_count(self):
        group_word_count, not_group_word_count = 0, 0
        word = []
        for i in range(self.N):
            word = self.words[i]
            for j in range(len(word) - 1):
                if word[j] != word[j + 1]:
                    new_word = word[j + 1:]
                    if new_word.count(word[j]) > 0:
                        not_group_word_count += 1
            if not_group_word_count == 0:
                group_word_count += 1
            not_group_word_count = 0
        print(group_word_count)
            

def main():
    N = int(input())
    words = []
    for i in range(N):
        word = input()
        words.append(word)
    word_count = group_word(N, words)
    word_count.word_count()
    
    
if __name__ == "__main__":
    main()
    


