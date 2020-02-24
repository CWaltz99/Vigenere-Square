from comparable import Comparable

class HuffElement(Comparable):
    """
    This class is used in conjunction with the HuffMap class.
    The HuffMap class is a dictionary for storing the frequency 
    counts of characters found in a string, and the Huffman code 
    for that character. The key for the HuffMap is the character 
    and the value is a HuffElement object, which contains the
    character, its frequency in the string, and its Huffman code.    
    """
    def __init__(self, char=""):
        """
        Create a HuffElement object for the passed in character.
        Initialize the character, the frequency to zero 
        and the code to the empty string.
        """
        self.ch = char
        self.ch_freq = 0
        self.code = ""
        
    def inc_freq(self):
        """
        Increment the character frequency count
        """
        
        self.ch_freq += 1
               
    def get_freq(self):
        """
        Return the character frequency count
        """
        
        return self.ch_freq
        
    def set_freq(self, count):
        """
        Set the character frequency count
        """
        
        self.ch_freq = count

    def get_char(self):
        """
        Return the character
        """
        
        return self.ch

    def set_char(self, char):
        """
        Set the character
        """
        
        self.ch = char
                  
    def get_code(self):
        """
        Return the Huffman code for the character
        """
        
        return self.code

    def set_code(self, code):
        """
        Set the Huffman code for the character
        """
        
        self.code = code
        
    def compare (self, other_huff_elem):
        """
        Use the character frequency count for comparison
        """
        
        return self.ch_freq - other_huff_elem.ch_freq
        
    def __str__(self):
        """
        Returns a string representation of this HuffElement
        """
        return "Char: " + self.ch + " Code: " + self.code + " Count: " + str(self.ch_freq)








