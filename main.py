


# a class to implement intuitive operators for 32 bit words
class Word :
    def __init__(self, val: int):
        self.val = val & 0xffffffff

    def __add__(self, other):
        theSum = Word( (self.val + other.val) & 0xffffffff )
        return (theSum)
    
    def __xor__(self, other):
        theXor = Word ( (self.val ^ other.val) & 0xffffffff )
        return (theXor)
    
    def __lshift__(self, anInt)
        theLshift = Word ( (self.val << anInt) & 0xffffffff)
        return (theLshift)

    def __rshift__(self, anInt)
        theRshift = Word ( (self.val >> anInt) & 0xffffffff)
        return (theLshift)
    
class WordGrid :
    def __init__(self, val: [int] ):
        self.