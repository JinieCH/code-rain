class WordManager(object):
    def __init__(self):
        self.totalWords = []
        self.MaxWords = 10
        self.displayWords = []
        self.matchingWords = []
        for i in range(0, self.MaxWords):
            self.push_word()

    def pop_word(self, i):
        self.matchingWords.append(i)
        self.displayWords.remove(i)

    def push_word(self):
        while True:
            w = self.totalWords[random.randint(0,25)]
            if self.stringCompare(w) == 0:
                self.displayWords.append(Word(w, random.randint(0, System.windowWidth-100), random.uniform(50,100)))
                break

    def stringCompare(self, v):
        for i in self.displayWords:
            if i.word == v:
                return i
        return 0
