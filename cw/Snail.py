
import unittest

def snail(array):
    
    if len(array) and len(array[0]) > 0:    
        result = [array[0][0]]
    else:
        return [] 
    done = [(0,0)]
    i, j = 0, 0
    
    def can_go_right(i, j):
        if (j + 1) < len(array[0]):
            if (not (i,j+1) in done):
                return True
        return False
    def can_go_down(i, j):
        if (i + 1) < len(array):
            if (not (i+1, j) in done):
                return True
        return False
    def can_go_left(i, j):
        if (j - 1) >= 0:
            if (not (i, j-1) in done):
                return True
        return False
    def can_go_up(i, j):
        if (i - 1) >= 0 :
            if (not (i-1,j) in done):
                return True
        return False


    while(True):
        moved = False
        while can_go_right(i, j):
            done.append((i, j+1))
            result.append(array[i][j+1])
            j+=1
            moved = True
        while can_go_down(i, j):
            done.append((i+1, j))
            result.append(array[i+1][j])
            i+=1
            moved = True
        while can_go_left(i, j):
            done.append((i, j-1))
            result.append(array[i][j-1])
            j-=1
            moved = True
        while can_go_up(i, j):
            done.append((i-1, j))
            result.append(array[i-1][j])
            i-=1
            moved = True
        if not moved: 
            return result     

class BobTests(unittest.TestCase):

    def test1(self):
        array = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEquals(snail(array), expected)
        array = [[1,2,3],
                 [8,9,4],
                 [7,6,5]]
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEquals(snail(array), expected)
        array = [[1],
                 [2],
                 [3]]
        expected = [1,2,3]
        self.assertEquals(snail(array), expected)
        array = []
        expected = []
        self.assertEquals(snail(array), expected)
        array = [[]]
        expected = []
        self.assertEquals(snail(array), expected)

        array = [[1,  2,   3, 4, 5], 
                 [6,  7,   8, 9, 10], 
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20], 
                 [21, 22, 23, 24, 25]] 
        expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
                    #[1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 17, 18, 19, 14, 13, 12, 11, 6, 7, 8, 9]
        self.assertEquals(snail(array), expected)
 
if __name__ == '__main__':
    unittest.main()
