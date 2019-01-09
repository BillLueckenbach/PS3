import unittest

# Import modules to be unit tested
from ps3 import get_word_score
from ps3 import update_hand
from ps3 import is_valid_word
from ps3 import load_words


word_list = load_words()    

# Define test class that inherits from unittest.testcase() #########
class test_ps3(unittest.TestCase):
    # Load valid words from ps3
    def test_get_word_score(self):
        # dictionary of words and scores
        words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
                 ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
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
        
        
    def test_is_valid_word(self):
        '''
        Unit Test for is_valid_word.  Tests adapted from homework tests.
        '''
        
        # Test "hello" in hand
        handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        handCopy = handOrig.copy()
        word = "hello"
        failure_message = f'''FAILURE: test_is_vaild_word()
                              \t Expected True, but got False for 
                              \t word: {word}, and 
                              \t hand: {handOrig}
                        '''
        self.assertTrue(is_valid_word(word, handCopy, word_list), 
                        failure_message)
        
        # Test a second time to see if word_list or hand has been modified
        failure_message += "\n\t when testing a second time"
        self.assertTrue(is_valid_word(word, handCopy, word_list),
                         failure_message)
        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're",
                  "not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig,
                  "but it is", handCopy)        
            
        # Test Rapture only 1 'r' in hand
        hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
        word = "Rapture"
        failure_message = f'''FAILURE: test_is_valid_word()
                              \tExpected False, but got True for 
                              word: {word} and 
                              hand: {hand}
                        '''                        
        self.assertFalse(is_valid_word(word, hand, word_list),
                         failure_message)
        
        # Test "honey" is in hand 
        hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
        word = "honey"
        failure_message = f'''FAILURE: test_is_valid_word()
                              \tExpected True, but got False for 
                              word: {word} and 
                              hand: {hand}    
                        '''
        self.assertTrue(is_valid_word(word, hand, word_list),
                         failure_message
                         )        
        
        # Test "honey" is not in hand afer honey passed
        hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
        word = "honey"
        failure_message = f'''FAILURE: test_is_valid_word()
                              \tExpected False, but got True for 
                              word: {word} and 
                              hand: {hand}    
                        '''
        self.assertFalse(is_valid_word(word, hand, word_list),
                         failure_message
                         )

        # Test "EVIL" is in hand checking caps
        hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
        word = "EVIL"
        failure_message = f'''FAILURE: test_is_valid_word()
                              \tExpected True, but got False for 
                              word: {word} and 
                              hand: {hand} 
                        '''
        self.assertTrue(is_valid_word(word, hand, word_list),
                         failure_message
                         )

        # Test "even" is not in hand only one 'e'
        hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
        word = "even"
        failure_message = f'''FAILURE: test_is_valid_word()
                              \tExpected False, but got True for 
                              word: {word} and 
                              hand: {hand} 
                        '''
        self.assertFalse(is_valid_word(word, hand, word_list),
                         failure_message
                         )








        
if __name__ == '__main__':
    unittest.main()
