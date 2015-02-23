from operator import itemgetter
from itertools import imap, groupby
def unique_in_order(iterable):
    return list(imap(next, imap(itemgetter(1), groupby(iterable))))


import unittest
class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(unique_in_order(''),[])
        self.assertEqual(unique_in_order('A'),['A'])
        self.assertEqual(unique_in_order('AA'),['A'])        
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'),['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order('ABBCcAD'),['A', 'B', 'C', 'c', 'A', 'D'])
        self.assertEqual(unique_in_order('AADD'),['A','D'])
        self.assertEqual(unique_in_order('AAD'),['A','D'])
        self.assertEqual(unique_in_order('ADD'),['A','D'])
        self.assertEqual(unique_in_order([1,2,3,3]),[1,2,3])
        self.assertEqual(unique_in_order([1,2,2,2,3,3]),[1,2,3])
        

if __name__ == '__main__':
    unittest.main()
    
    
    
#     test.assert_equals(unique_in_order(''),[])
# test.assert_equals(unique_in_order('A'),['A'])
# test.assert_equals(unique_in_order('AA'),['A'])        
# test.assert_equals(unique_in_order('AAAABBBCCDAABBB'),['A', 'B', 'C', 'D', 'A', 'B'])
# test.assert_equals(unique_in_order('ABBCcAD'),['A', 'B', 'C', 'c', 'A', 'D'])
# test.assert_equals(unique_in_order('AADD'),['A','D'])
# test.assert_equals(unique_in_order('AAD'),['A','D'])
# test.assert_equals(unique_in_order('ADD'),['A','D'])
# 
# 
# Implement the function unique_in_order which takes as argument a string and returns a list of items without duplicates elements next to each other preserving the original order.
# 
# For example: 
# # unique_in_order('AAAABBBCCDAABBB') --> A B C D A B
# # unique_in_order('ABBCcAD') --> A B C A D
# test.assert_equals(unique_in_order('AAAABBBCCDAABBB'),['A', 'B', 'C', 'D', 'A', 'B'])
# test.assert_equals(unique_in_order('ABBCcAD'),['A', 'B', 'C', 'c', 'A', 'D'])
# 
# 
# ...     