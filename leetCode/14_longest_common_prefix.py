class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs or len(strs) == 0:
            return ''
        prefix = strs[0]
        for str in strs[1:]:
            i = 0
            while(True):
                if i < len(str) and i < len(prefix):
                    if str[i] == prefix[i]:
                        i+=1
                    else:
                        break
                else:
                    break
            prefix = prefix[:i]
            
        return prefix
            
                
                
assert '' == Solution().longestCommonPrefix(None)   
assert '' == Solution().longestCommonPrefix([])   
assert 'aa' == Solution().longestCommonPrefix(['aa'])   
assert '' == Solution().longestCommonPrefix(['aa','bb'])   
assert 'a' == Solution().longestCommonPrefix(['ab', 'aa'])   
assert 'a' == Solution().longestCommonPrefix(['ab', 'a'])   
assert 'a' == Solution().longestCommonPrefix(['ab', 'a'])   
assert 'a' == Solution().longestCommonPrefix(['a', 'ab'])   
assert 'abc' == Solution().longestCommonPrefix(['abc', 'abc'])   
assert 'abc' == Solution().longestCommonPrefix(['abc', 'abcd'])   
assert 'ab' == Solution().longestCommonPrefix(['abc', 'abcd', 'ab', 'abcd'])   
assert '' == Solution().longestCommonPrefix(['', '', '', 'abcd'])   
