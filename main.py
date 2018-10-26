


# a class to implement intuitive operators for 32 bit words
class Word :
    def __init__(self, val):
        self.val = val & 0xffffffff
    def __add__(self, otherWord):
        sum = Word( (self.val + otherWord.val) & 0xffffffff )
        return (self.val + otherWord.val)