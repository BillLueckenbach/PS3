import unittest

# Import modules to be unit tested
from ps3 import get_word_score
from ps3 import update_hand

#

# Define test class that inherits from unittest.testcase() #########
class test_ps3(unittest.TestCase):
    
    def test_get_word_score(self):
        # dictionary of words and scores
        words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
                 ("scored", 7):351, ("WaYbILl", 7):734, ("Outgnaw", 7):539,
                 ("fork", 7):209, ("FORK", 4):308}
        for (word, n) in words.keys():
            score = get_word_score(word, n)
            failure_message = (f"FAILURE: test_get_word_score()\n" 
                               f"\tExpected {words[(word, n)]} points but got\n"
                               f"\t{str(score)} for word '{word}', n={str(n)}"
                              )
            self.assertEqual(score, 
                             words[(word, n)],
                             failure_message
                            ) 
    # end of test_get_word_score


    def test_update_hand(self):
        """
        Unit test for update_hand
        """
        # test 1
        handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
        handCopy = handOrig.copy()
        word = "quail"

        updated_hand = update_hand(handCopy, word)
        expected_hand = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
        # Check proper response
        self.assertEqual(updated_hand, expected_hand)
        # Check did not modify handCopy
        self.assertEqual(handCopy, handOrig)
        
        # test 2
        handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
        handCopy = handOrig.copy()
        word = "Evil"

        updated_hand = update_hand(handCopy, word)
        expected_hand = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
        #check proper response with capital letter in word
        self.assertEqual(updated_hand, expected_hand)
        #Check did not modify handCopy
        self.assertEqual(handCopy, handOrig)

        # test 3
        handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        handCopy = handOrig.copy()
        word = "HELLO"

        updated_hand = update_hand(handCopy, word)
        expected_hand = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
        #Check proper response with all CAPS word
        self.assertEqual(updated_hand, expected_hand)
        #Check did not modify handCopy
        self.assertEqual(handCopy, handOrig)

# end of test_update_hand


if __name__ == '__main__':
    unittest.main()
